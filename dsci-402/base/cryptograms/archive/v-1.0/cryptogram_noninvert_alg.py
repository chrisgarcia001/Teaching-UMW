import copy

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
def decode(code, key):
	word = ''
	for lett in code:
		if lett in key.keys():
			word += key[lett]
		else:
			word += '.'
	return word

# Get all elements in d1 not in d2.	
def dict_diff(d1, d2):
	d3 = copy.copy(d1)
	for k in d2.keys():
		del d3[k]
	return d3

def dict_union(d1, d2):
	return dict(d1, **d2)
	
# This class holds a list of words and facilitates caching of match operations.	
class WordList:
	def __init__(self, filename):
		self.all_words = map(lambda x: x.lower(), read_words(filename))
		self.length_cache = {}
		self.match_cache = {}
	
	# Returns list of strings matching the pattern. Uses a multi-strategy caching scheme to
	# cut down on unnecessary repeated computation.
	def get_matches(self, pattern):
		if self.match_cache.has_key(pattern):
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
	
	# Get a hashable value.
	def __hash__(self):
		return hash(self.code)
		
	def __str__(self):
		return "Code: " + str((self.code, self.word))

# Find a dict key that matches the code words.	
def find_key(open_codes, word_list, master_key = {}):
	for cw in open_codes:
		cw.set_vars(master_key)
	closed = filter(lambda x: not(x.is_open()), open_codes)
	still_open = filter(lambda x: x.is_open(), open_codes)
	non_words = filter(lambda x: not(word_list.has_word(x)), map(lambda y: y.word, closed))
	if len(non_words) > 0:
		return None
	if len(still_open) == 0:
		return master_key
	next = list(still_open)[0]
	matches = word_list.get_matches(next.word)
	for match in matches:
		next.set_vars(master_key)
		next_vars = next.get_new_vars(match)
		sol = find_key(still_open, word_list, dict_union(master_key, next_vars))
		if sol != None:
			return sol
	return None

	
	
	
		