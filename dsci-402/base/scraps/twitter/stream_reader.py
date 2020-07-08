# ---------------------------------------------------------------------
# Author: cgarcia
# About: This is a simple modification of the tweepy streaming example.
#        I added the use of the property file for storing account info.
# ---------------------------------------------------------------------

import sys
import json
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from twitter_util import read_props

prop_file = 'account_info.txt'
if(len(sys.argv) > 1):
	prop_file = sys.argv[1]
props = read_props(prop_file)

# Go to http://dev.twitter.com and create an app.
# The consumer key and secret will be generated for you after
consumer_key = props['consumer_key']
consumer_secret = props['consumer_secret']

# After the step above, you will be redirected to your app's page.
# Create an access token under the the "Your access token" section
access_token = props['access_token']
access_token_secret = props['access_token_secret']

class StdOutListener(StreamListener):
	""" A listener handles tweets are the received from the stream.
    This is a basic listener that just prints received tweets to stdout.
    
    """
	
	def on_data(self, data):
		#print(unicode(data).encode('utf-8'))
		#print(unicode(data).encode('utf-8'))
		#print(data.encode('utf-8'))
		print(json.loads(data)['text'].encode('utf-8'))
		return True
	'''
	def on_status(self, status):
		print(unicode(status.text).encode('utf-8'))
		#print(type(status))
		return True
	'''	
	def on_error(self, status):
		print status
		return True
		
# initialize blank list to contain tweets
tweets = []
# file name that you want to open is the second argument
save_file = open('9may.json', 'a')

class CustomStreamListener(StreamListener):
	def __init__(self, api):
		self.api = api
		super(StreamListener, self).__init__()
		#self.save_file = tweets
		
	def on_data(self, tweet):
		#print(tweet)
		print(json.loads(tweet)['text'].encode('utf-8'))
		#print(json.loads(tweet.decode('utf-16')))
		#self.save_file.append(json.loads(tweet))
		#print tweet
		#save_file.write(str(tweet))
		
if __name__ == '__main__':
	l = StdOutListener()
	auth = OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)
	
	stream = Stream(auth, l)
	stream.filter(track = ['fun'], languages = ['en'])#['basketball'])
	#stream.sample()