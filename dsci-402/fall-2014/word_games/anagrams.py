# Takes filename of word list as input and returns 
# these wordsin a python list.
def read_words(filename):
	words = open(filename, 'r').readlines()
	return filter(lambda x: x != '', map(lambda y: y.strip().lower(), words))

# For each letter, determine the number of occurrences in the word.	
def word_histogram(word):
	hist = {}
	for char in word:
		if not(hist.has_key(char)):
			hist[char] = 1
		else:
			hist[char] += 1
	return hist		

# Find all anagrams for the given word inside the word list.	
def anagrams(word, word_list):
	hist = word_histogram(word)
	found = []
	for w in word_list:
		if hist == word_histogram(w):
			found.append(w)
	return found