from twitter_util import *

# Returns a list of commonly-used punctuation.
def standard_punct_list():
	return ['.', '?', ',', '-', "'", '"', ';', ':', '/', "\t", "\n", '!']

# Returns a space if a char is deemed to be punctuation.
def remove_punct(char, punct):
	if char in punct:
		return ' '
	return char
		
# Reads in a file of sentiment code words and parses
# out into a dict.
def get_sentiment_codes(filename):
	lines = open(filename, 'r').readlines()
	codes = {}
	for line in lines:
		words = line.lower().strip().replace("\t", ' ').replace("\n", ' ').split(' ')
		words = filter(lambda x: x != '', words)
		code = float(words[len(words) - 1])
		codes[words[0]] = code
	return codes

# For a passage of text, builds tuple of form
# (total_word_count, sentiment_word_count, sentiment_score_total).	
def sentiment_tuple(codes, text, punct = standard_punct_list()):
	clean_text = ''.join(map(lambda x: remove_punct(x, punct), text)).lower()
	words = filter(lambda x: x != '', clean_text.split(' '))
	total_word_count = len(words)
	sentiment_word_count = 0
	sentiment_score_total = 0
	for word in words:
		if codes.has_key(word):
			sentiment_word_count += 1
			sentiment_score_total += codes[word]
	return (total_word_count, sentiment_word_count, sentiment_score_total)

# Perform sentiment scoring on a passage of text.
def sentiment_score(codes, text, normalize_all_words = True, punct = standard_punct_list()):
	twc, swc, sc = sentiment_tuple(codes, text, punct)
	denom = twc
	if not(normalize_all_words):
		denom = swc
	if denom == 0:
		return 0
	return float(sc) / float(denom)