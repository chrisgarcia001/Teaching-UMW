from twitter_util import *
from sentiment import *

tweets = read_tweets("tweet_data/11.12.txt")
states = read_states("data/states.txt")

for t in tweets[:100]:
	try:
		print(extract_state(states, text(t, ['user', 'location'])))
	except:
		print("UNREADABLE")
