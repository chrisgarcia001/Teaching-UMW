import tweepy
from twitter_util import read_props

props = read_props('secret_account_info.txt')

consumer_key = props['consumer_key']
consumer_secret = props['consumer_secret']
access_token = props['access_token']
access_token_secret = props['access_token_secret']

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
for tweet in tweepy.Cursor(api.search,
							q="google",
							rpp=100,
							result_type="recent",
							include_entities=True,
							lang="en").items():
	try:
		print(unicode(tweet.text).encode('ascii', 'ignore'))
	except: 
		print('bad text')
