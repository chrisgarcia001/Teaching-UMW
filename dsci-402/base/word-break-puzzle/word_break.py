# This solves the following problem, taken from the 
# following URL: http://thenoisychannel.com/2011/08/08/retiring-a-great-interview-problem

# -------------------- PROBLEM ----------------------------
# Given an input string and a dictionary of words,
# segment the input string into a space-separated
# sequence of dictionary words if possible. For
# example, if the input string is "applepie" and
# dictionary contains a standard set of English words,
# then we would return the string "apple pie" as output.
# ----------------------------------------------------------

# This solution will find every possible segmentation. 
# Returns a list of lists of words.
def word_breaks(word, word_list):
	if len(word) == 0:
		return [[]]
	prefixes = filter(lambda w: word.startswith(w), word_list)
	if len(prefixes) == 0:
		return None
	suffixes = map(lambda y: word[len(y):], prefixes)
	pairs = filter(lambda (x, y): y != None, zip(prefixes, map(lambda w: word_breaks(w, word_list), suffixes)))
	if len(pairs) == 0:
		return None
	combine = lambda (front, backs): map(lambda x: [front] + x, backs)
	return reduce(lambda x, y: x + y, map(combine, pairs))
	