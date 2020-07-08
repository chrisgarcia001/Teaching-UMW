# ---------------------------------------------------------------------
# Author: cgarcia
# About: This provides some utilities for text sentiment-scoring.
# ---------------------------------------------------------------------

import nltk
from nltk.corpus import stopwords # NOTE: do > nltk.download() first

# Read in a sentiment code word file consisting of a <word> <score> on 
# each line and get the resulting codes as a dict.
def sentiment_codes(filename):
	codes = {}
	lines = open(filename, 'r').readlines()
	for line in lines:
		text = filter(lambda x: x != '', line.lower().strip().replace("\t", " ").split(' '))
		word = ' '.join(text[:(len(text) - 1)])
		score = float(text[len(text) - 1])
		codes[word] = score 
	return codes

# Produce a score tuple: (total sentiment words, total sentiment value sum)
def sentiment_tuple(text, codes):
	words = nltk.word_tokenize(text.lower())
	occurrences = 0
	val = 0
	for word in words:
		if codes.has_key(word):
			val += codes[word]
			occurrences += 1
	return (occurrences, val)

# Get a single sentiment score for the text passage - sum of points/num. sentiment words.	
def sentiment(text, codes):
	(occ, total) = sentiment_tuple(text, codes)
	if occ > 0:
		return float(total) / float(occ)

# For words not in the sentiment list, derive a sentiment score based on 
# overall occurrence with scored words.		
def infer_word_sentiments(text_passages, codes):
	sentiments = map(lambda x: sentiment(x, codes), text_passages)
	sentiment_words = set(codes.keys())
	punct = ['.', '!', '?']
	words = {}
	for t in text_passages:
		curr_text = set(nltk.word_tokenize(t.lower())).difference(sentiment_words.union(set(punct)))
		tuple = sentiment_tuple(t, codes)
		for word in curr_text:
			if not(words.has_key(word)):
				words[word] = []
			words[word].append(tuple)
	word_sentiments = {}
	for (word, tuples) in words.items():
		tuples.append((0,0))
		(occ_total, score_total) = reduce(lambda (w,x),(y,z): (w + y, x + z), tuples)
		if occ_total > 0:
			word_sentiments[word] = float(score_total) / float(occ_total)
		else:
			word_sentiments[word] = 0.0
	return word_sentiments
		
		
	