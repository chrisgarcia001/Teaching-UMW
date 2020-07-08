import json
import simplejson as sj
import re
import unicodedata

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
			print("no")
	return tweets
	

	
	
	
	
	