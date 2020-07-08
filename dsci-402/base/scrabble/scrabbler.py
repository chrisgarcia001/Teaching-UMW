# Read in a file of words with one word per line and get the list of words.
def read_words(filename):
	return filter(lambda y: len(y) > 0, map(lambda x: x.strip().lower(), open(filename).readlines()))	

# Construct a histogram dict of the count of each unique letter in the word	
def letter_histogram(word):
	h = {}
	for lett in map(lambda x: x, word):
		k = lett.lower()
		if not(h.has_key(k)):
			h[k] = 1
		else:
			h[k] += 1
	return h

# Is the subbag contained within the superbag?	
def is_sub_bag(subbag, superbag):
	h1 = subbag
	if not(type(h1)) == type({}):
		h1 = letter_histogram(subbag)
	h2 = superbag 
	if not(type(h2)) == type({}):
		h2 = letter_histogram(superbag)
	for (lett, count) in h1.items():
		if not(h2.has_key(lett)) or h2[lett] < count:
			return False
	return True

# For the given "word" - i.e. letters and word-list, find all words at 
# most max_length containing all letters in word.	
def scrabbler(word, word_list, max_word_length):
	word = letter_histogram(word)  # Make it faster here
	matches = filter(lambda x: is_sub_bag(word, x), word_list)
	return filter(lambda x: len(x) <= max_word_length, matches)

# Find all words in word_list that are anagrams of word.	
def anagrams(word, word_list):
	return scrabbler(word, word_list, len(word))
	
	