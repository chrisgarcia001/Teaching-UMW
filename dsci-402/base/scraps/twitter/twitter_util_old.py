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
	
def read_tweets_old(filename):	
	#lines = open(filename, 'r').readlines()
	#return lines
	#return map(lambda tw: json.load(unicode(tw).encode('utf-8')), lines)
	#print(open(filename, 'r').read())
	#data = open(filename, 'rb').read().decode('utf-8')
	data = filter(lambda x: x != '', open(filename, 'r').readlines())
	data = map(lambda x: x.decode('utf-8'), data)
	#return data.split("\n")
	return map(lambda x: json.loads(x), data)
	#return 
	
def read_tweets_2(filename):	
	data = open(filename, 'rb').read().decode('utf-16')
	#print(data)
	cleaned = ','.join(filter(lambda x: x != '', data.split("\n")))
	print(cleaned)
	return json.loads('[' + cleaned + ']')

def read_tweets_3(filename):	
	data = open(filename, 'rb').read().decode('utf-16')
	#print(data)
	clean_keyws = lambda x: x.replace(':true', ':True').replace(':false', ':False').replace(':null',':None')
	cleaned = ','.join(filter(lambda x: x != '', map(clean_keyws, data.split("\n"))))
	#cleaned = filter(lambda x: x != '', map(clean_keyws, data.split("\n")))
	print(cleaned)
	#data = filter(lambda x: x != '', open(filename, 'r').readlines())
	#data = map(lambda x: x.decode('utf-8'), data)
	#return data.split("\n")
	#return map(lambda x: json.loads(x), data)
	#return eval('[' + cleaned + ']')
	#return map(lambda x: eval(x), cleaned)
	return json.loads('{"tweets":[' + cleaned + ']}')['tweets']
	
def read_tweets(filename):
	tweet_file = open(filename)                        
	#tweet_hash = {}     
	tweets = []
	bad = 0
	for tweet_line in tweet_file: 
		try:
			tweet = json.loads(tweet_line) 
			tweets.append(tweet)
		except:
			bad += 1
	print(bad)
	return tweets
		

def read_tweets_4(filename):
	raw_tweets = open(filename).readlines()
	print(raw_tweets[0])
	return map(lambda x: json.loads(x.strip()), raw_tweets)
		
def parse_tweets(tweet_file_path):
    raw_tweets = open(tweet_file_path)
    tweets = []
    for line in raw_tweets:
		try:
			#tw = unicodedata.normalize('NFKD', line).encode('ascii','ignore')
			parsed_tweet = json.loads(line)
			text = ''
			if parsed_tweet.has_key('text'):
				text = parsed_tweet['text']
			#tweets += [text.lower()]
			tweets += [text]
		except:
			3 == 3
    return tweets

def read_tweets_5(filename):	
	data = open(filename, 'rb').read().decode('utf-16')
	#print(data.split("\n")[0].strip())
	print(json.loads(data.split("\n")[0].strip()))
	cleaned = data.replace("}\n{","},{").replace("}{","},{")
	cleaned = cleaned.replace("}\n\n{","},{").replace("}\n\n\n{","},{")
	#print(data.split("\n")[0])
	#print('[' + cleaned + ']')
	#return json.loads('[' + data.replace("}\n{","},{") + ']')
	
def read_tweets_6(filename):	
	data = open(filename, 'rb').read().decode('utf-16').split("\n")
	tweets = []
	for line in data:
		try:
			tweets.append(json.loads(line.strip()))
		except:
			print("no")
	return tweets
	
'''	
def tweets(filename):
	raw_tweets = open(filename).readlines()
	return map(lambda x: eval(x.encode('utf-8').strip()), raw_tweets)
'''

# -----------------------------
invalid_escape = re.compile(r'\\[0-7]{1,6}')  # up to 6 digits for codepoints up to FFFF

def replace_with_codepoint(match):
    return unichr(int(match.group(0)[1:], 8))


def repair(brokenjson):
    return invalid_escape.sub(replace_with_codepoint, brokenjson)
	
def tweets(filename):
	raw_tweets = open(filename).readlines()
	tweets = []
	for tweet in raw_tweets:
		#tweet = tweet.encode('utf-8')
		tweets.append(repair(json.loads(tweet)))
	return tweets
	
	
	
	
	
	