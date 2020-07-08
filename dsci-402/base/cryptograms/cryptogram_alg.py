#-----------------------------------------------------------------------------
# Author: cgarcia
# About: This file contains an invertible cryptogram solver (i.e. each
#        letter in unencrypted word has exactly one code letter mapping
#        to it). 
#------------------------------------------------------------------------------

#-----------------------------------------------------------------------------
# SECTION 1: General utility functions
#-----------------------------------------------------------------------------

# Read in a file of words with one word per line and get the list of words.
def read_words(filename):
	return filter(lambda y: len(y) > 0, map(lambda x: x.lower().strip(), open(filename).readlines()))

# Does the pattern match the word? A pattern is of the form "m..y", where "." are open to instantiation. 
def is_match(pattern, word):
	if len(pattern) != len(word):
		return False
	else:
		for (x, y) in zip(pattern, word):
			if x != '.' and x != y:
				return False
	return True	

# For a given pattern and set of superpatterns, find the closest matching superpattern
# Ex: closest_superpattern("ma.y", ["...y", "m..y", "da..", ".a.y"]) => "m..y"
def closest_superpattern(pattern, superpatterns):
	curr = None
	best = len(pattern)
	for super in superpatterns:
		if is_match(super, pattern):
			dots = len(filter(lambda x: x == '.', super))
			if curr == None or dots < best:
				curr = super
				best = dots
	return curr

# Using the dict key, return the decoding of the code specified.
def decode(code, key, nonmatch_passthru = False):
	word = ''
	for lett in code:
		if lett in key.keys():
			word += key[lett]
		elif nonmatch_passthru:
			word += lett
		else:
			word += '.'
	return word

# Assuming a dict is invertible, return its inverse. If not then given the
# (key, val) pair, the last occurrence of val's key will be the inverse value.
def dict_inverse(some_dict):
	return dict((v,k) for k, v in some_dict.iteritems())

# Get the union between 2 dicts.
def dict_union(d1, d2):
	return dict(d1, **d2)

#-----------------------------------------------------------------------------
# SECTION 2: WordList class. 
# This class holds a list of words and facilitates caching of match operations.
# The caching cuts down on time required to compute matches.
#-----------------------------------------------------------------------------		
class WordList:
	def __init__(self, filename):
		self.all_words = map(lambda x: x.lower(), read_words(filename))
		self.length_cache = {}
		self.match_cache = {}
	
	# Returns list of strings matching the pattern. Uses a multi-strategy caching scheme to
	# cut down on unnecessary repeated computation.
	def get_matches(self, pattern):
		if self.match_cache.has_key(pattern):
			matches = self.match_cache[pattern]
			return self.match_cache[pattern]
		sp = closest_superpattern(pattern, self.match_cache.keys())
		if sp != None:
			matches = filter(lambda x: is_match(pattern, x), self.match_cache[sp])
			self.match_cache[pattern] = matches
			return matches
		if not(self.length_cache.has_key(len(pattern))):
			self.length_cache[len(pattern)] = filter(lambda x: len(x) == len(pattern), self.all_words)
		matches = filter(lambda x: is_match(pattern, x), self.length_cache[len(pattern)])
		self.match_cache[pattern] = matches
		return matches
	
	# Is the word specified found in this list?
	def has_word(self, word):
		if not(self.length_cache.has_key(len(word))):
			self.length_cache[len(word)] = filter(lambda x: len(x) == len(word), self.all_words)
		return word in self.length_cache[len(word)]

#-----------------------------------------------------------------------------
# SECTION 3: CodeWord class. 
# This class keeps track of a code and its corresponding word. A CodeWord 
# has 2 parts: the code string and the word string. Initally there is nothing
# in the word string (just string of "." of same length as code). This class
# supports the instantiation of code -> word letter variables in searching for 
# solutions. A variable set is just a dict of form {code_letter : word_letter}. 
#-----------------------------------------------------------------------------			
class CodeWord:
	def __init__(self, code):
		self.code = code
		self.word = ''.join(map(lambda x: '.', code))
		self.vars = {}
	
	# How many remaining characters are there to be set?
	def open_chars(self):
		return len(filter(lambda x: x == '.', self.word))
	
	# Are there any uninstantiated code characters?
	def is_open(self):
		return self.open_chars() > 0
	
	# Get the new instantiated variables not already contained in master key
	def get_new_vars(self, matching_word):
		pos = filter(lambda i: self.word[i] == '.', range(0, len(self.word)))
		h = {}
		for i in pos:
			h[self.code[i]] = matching_word[i]
		return h
	
	# Update the variable set and decode accordingly.
	def set_vars(self, new_vars):
		self.vars = new_vars
		self.word = decode(self.code, self.vars)

#-----------------------------------------------------------------------------
# SECTION 4: Consistency-checking functions
#-----------------------------------------------------------------------------
		
# This is to ensure the invertible consistency of a pattern and matching word.
# The inv_map is the inverse mapping of the variables.
def is_consistent(inv_map, code, matching_word):
	for (clett, wlett) in zip(code, matching_word):
		if inv_map.has_key(wlett) and inv_map[wlett] != clett:
			return False
	return True

# For a given codeword, word_list, and pre-set vars, find all matches consistent
# with the inverse vars.	
def get_consistent_matches(inv_map, codeword, word_list):
	matches = word_list.get_matches(codeword.word)
	return filter(lambda x: is_consistent(inv_map, codeword.code, x), matches)
	
#-----------------------------------------------------------------------------
# SECTION 5: Main algorithms
#-----------------------------------------------------------------------------

# This is the core algorithm - Find a dict key that matches the code words.	
def find_key(open_codes, word_list, master_key = {}):
	for cw in open_codes:
		cw.set_vars(master_key)
	closed = filter(lambda x: not(x.is_open()), open_codes)
	still_open = filter(lambda x: x.is_open(), open_codes)
	non_words = filter(lambda x: not(word_list.has_word(x)), map(lambda y: y.word, closed))
	inv = dict_inverse(master_key)
	bad = filter(lambda x: not(word_list.has_word(x.word)) or not(is_consistent(inv, x.code, x.word)), closed)
	if len(bad) > 0:
		return None
	if len(still_open) == 0:
		return master_key
	next = list(still_open)[0]
	matches = get_consistent_matches(inv, next, word_list)
	for match in matches:
		next.set_vars(master_key)
		next_vars = next.get_new_vars(match)
		sol = find_key(still_open, word_list, dict_union(master_key, next_vars))
		if sol != None:
			return sol
	return None



	
	
		