### code to save tweets in json###
import sys
import tweepy
import json

consumer_key = "bIykEnQ31DuA4rRMOIHeiw"
consumer_secret = "wU14CMsjOan7XvZCxKYissclx1CYmYmQAILHRhFE"
access_key = "1403937170-uVXWEuzrUnMHFYmFDIyhsJWkc0I1B5Rx9OhxVXy"
access_secret = "GuEoUMBWrfPXLQgbGR90EW4BuPwc6cnAhmlKGOnDpU"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)
file = open('today.txt', 'a')

class CustomStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        print status.text

    def on_data(self, data):
		json_data = json.loads(data)
		string = json.dumps(json_data)
		nj = json.loads(string)
		print(string)
		#file.write(str(json_data))
		#file.write(string)
		#json.dump(string, file, ensure_ascii=False).encode('utf8')

    def on_error(self, status_code):
        print >> sys.stderr, 'Encountered error with status code:', status_code
        return True # Don't kill the stream

    def on_timeout(self):
        print >> sys.stderr, 'Timeout...'
        return True # Don't kill the stream

sapi = tweepy.streaming.Stream(auth, CustomStreamListener())
sapi.filter(track=['fun'], languages = ['en'])