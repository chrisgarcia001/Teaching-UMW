# ---------------------------------------------------------------------
# Author: cgarcia
# About: This is a simple modification of the tweepy streaming example.
#        I added the use of the property file for storing account info.
#        I also added a little extra command-line option processing to
#        allow random sampling or tweet gathering based on keywords.
# ---------------------------------------------------------------------

import sys
import json
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from twitter_util import read_props

def print_usage():
	text = 'usage: > python stream_reader [-u]\n'
	text += ' [-access <account file - default is "account_info.txt">]\n'
	text += ' [-track <topics to track - default is anything and any language>]'
	print(text)
	
try:
	if '-u' in sys.argv or '-usage' in sys.argv:
		raise 'print usage'
	prop_file = 'account_info.txt'
	if '-access' in sys.argv:
		prop_file = sys.argv[sys.argv.index('-access') + 1]
	props = read_props(prop_file)
	tracking = []
	if '-track' in sys.argv:
		tracking = sys.argv[(sys.argv.index('-track') + 1):]

	# Go to http://dev.twitter.com and create an app.
	# The consumer key and secret will be generated for you after
	consumer_key = props['consumer_key']
	consumer_secret = props['consumer_secret']

	# After the step above, you will be redirected to your app's page.
	# Create an access token under the the "Your access token" section
	access_token = props['access_token']
	access_token_secret = props['access_token_secret']

	class StdOutListener(StreamListener):
		def on_data(self, data):
			json_data = json.loads(data)
			string = json.dumps(json_data)
			nj = json.loads(string)
			print(string)
		
	if __name__ == '__main__':
		l = StdOutListener()
		auth = OAuthHandler(consumer_key, consumer_secret)
		auth.set_access_token(access_token, access_token_secret)
		
		stream = Stream(auth, l)
		if len(tracking) > 0:
			stream.filter(track = tracking, languages = ['en'])
		else:
			stream.sample()
except:
	print_usage()
	
