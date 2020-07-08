# ---------------------------------------------------------------------
# Author: cgarcia
# About: This provides a few basic utilities for reading tweets from 
#        json-based tweet files. 
# ---------------------------------------------------------------------

import json

# Read in a properties file (key:val pairs) and return a corresponding dict.
def read_props(filename, sep = '='):
	whitespace = [" ", "\t", "\n"]
	clean = lambda x: filter(lambda y: not(y in whitespace), x)
	split = lambda x: tuple(clean(x).split(sep))
	return dict(map(split, open(filename, 'r').readlines()))
	
# Read tweets as JSON objects from a file of json tweets.	
def read_tweets(filename):	
	data = open(filename, 'rb').read().decode('utf-16').split("\n")
	tweets = []
	for line in data:
		try:
			tweets.append(json.loads(line.strip()))
		except:
			print("JSON-unopenable tweet encountered")
	return tweets

# For a file of tweets, extract out the text portion of each.
def read_texts(filename):
	tweets = read_tweets(filename)
	text = []
	for tweet in tweets:
		try:
			text.append(unicode(tweet['text']).encode('ascii', 'ignore'))
		except:
			1 == 1
	return text

# Extract as text the specified object(by 'path') from the json tweet.
# The path is like a file path in the form of a list. If the path is
# only one level deep you don't need to put in a list. 
def text(json_tweet, path = 'text'):
	if type(path) != type([]):
		path = [path]
	try:
		depth = 0
		curr_obj = json_tweet
		while depth < len(path):
			curr_obj = curr_obj[path[depth]]
			depth += 1
		return unicode(curr_obj).encode('ascii', 'ignore')
	except:
		return None
	
	
	
	
	