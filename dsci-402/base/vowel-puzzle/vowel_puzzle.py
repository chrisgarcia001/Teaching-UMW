#--------------------------------------------------------------------------
# Author: cgarcia@umw.edu
# About: Imagine we are given 1) a dictionary of words, and 
#        2) a coded message. The coding is as follows: the message has all 
#        vowels, punctuation, and spaces between words removed. Our job 
#        is to recreate all possible decodings of this message.
#--------------------------------------------------------------------------

# Read in a file of words with one word per line and get the list of words.
def read_words(filename):
	return filter(lambda y: len(y) > 0, map(lambda x: x.strip().lower(), open(filename).readlines()))	

# Take real text and compress it to remove vowels and spaces.	
def compress(text):
	to_remove = ' aeiou'
	return filter(lambda x: not(x in to_remove), text.lower())

# For a dictionary or words and a single string without spaces, construct all
# possible ways break text into a sequence of real words through adding spaces.
# Example:  all_splits(<word list>, 'thisistext') 
#            => [['this', 'is', 'text']] # only one real way to break up 
def all_splits(words, text, cache = {}):
	if cache.has_key(text): return cache[text]
	if len(text) == 0: return [[]]
	prefix_matches = filter(lambda x: text.startswith(x), words)
	if len(prefix_matches) == 0: return None
	suffix = lambda prefix: text[len(prefix):]
	endings = map(lambda y: all_splits(words, suffix(y), cache), prefix_matches)
	pairs = filter(lambda (x,y): y != None, zip(prefix_matches, endings))
	if len(pairs) == 0: return None
	combine = lambda (prefix, suffixes): map(lambda x: [prefix] + x, suffixes)
	result = reduce(lambda x, y: x + y, map(combine, pairs))
	cache[text] = result
	return result

# Using a dictionary of full words, construct a map of form 
# {compressed_word: [<full word 1>, <full word 2>, ..]}
# which maps a compressed form of word to all matching full words.
def build_compression_map(words):
	cmap = {} # compressed_word : [<full word 1>, <full word 2>, ..]
	for word in words:
		cmp = compress(word)
		if not(cmap.has_key(cmp)): cmap[cmp] = []
		cmap[cmp].append(word)
	del(cmap[''])
	return cmap

# Given a compression map and a sequence of compressed words, find every possible
# decompressed rendering. 
# Example:  all_decompressions(<compr. map>, ['nrgtc', 'flbgs'])
# 	          => [['energetic', 'filibegs'], ['energetic', 'fleabags']]
def all_decompressions(comp_map, comp_word_seq):
	if len(comp_word_seq) == 0: return []
	if len(comp_word_seq) == 1: return map(lambda x: [x], comp_map[comp_word_seq[0]])
	curr = comp_map[comp_word_seq[0]]
	nxt = all_decompressions(comp_map, comp_word_seq[1:])
	return reduce(lambda w,x: w+x, map(lambda y: map(lambda z: [y] + z, nxt), curr))

# Solve the puzzle given the wordlist and coded/compressed text. Returns a
# list of lists, where each inner list is a feasible decompression.	
def solve(wordlist, compressed_text):
	cmap = build_compression_map(wordlist)
	compressed_words = cmap.keys()
	splits = all_splits(compressed_words, compressed_text)
	if splits == None: return None
	return reduce(lambda x,y: x+y, map(lambda z: all_decompressions(cmap, z), splits))
	
	
	