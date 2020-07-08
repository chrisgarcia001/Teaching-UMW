from twitter import TwitterStream, OAuth
from twitter_util import *
import sys


prop_file = 'account_info.txt'
if(len(sys.argv) > 1):
	prop_file = sys.argv[1]
props = read_props(prop_file)

auth = OAuth(
	props['access_token'],
	props['access_token_secret'],
	props['consumer_key'],
	props['consumer_secret']
)
twitter_stream = TwitterStream(auth=auth, domain='userstream.twitter.com')
sample = twitter_stream.statuses.sample()
for tweet in sample:
	#print(str(dict(tweet)))
	#print(str(tweet).encode('utf-8'))
	#print(tweet.keys())
	if tweet.has_key('text'):
		print(tweet['text'].encode('utf-8'))
	
