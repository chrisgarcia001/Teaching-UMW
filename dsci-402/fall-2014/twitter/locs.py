from twitter_util import *
from sentiment import *

tweets = read_tweets("tweet_data/11.12.txt")

for t in tweets:
	try:
		print(text(t, ['user', 'location']))
	except:
		print("UNREADABLE")