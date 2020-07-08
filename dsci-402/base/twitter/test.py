from twitter_util import *
from sentiment import *

print(read_props('account_info.txt'))
#print(read_tweets('tweets.txt')[0])
#print(read_texts('tweets.txt'))
tweets = read_tweets('tweet_data/tweets1.txt')[0:5]
for t in tweets:
	print(text(t))
	print('  Location: ' + text(t, ['user', 'location']) or 'None')
	print('  Source: ' + text(t, 'source') or 'None')
	
codes = sentiment_codes('data/AFINN-111.txt')
for item in codes.items()[:5]:
	print(item)
	
for t in tweets:
	print(text(t) + ': ' + str(sentiment_tuple(text(t), codes)))
	
print(infer_word_sentiments(map(lambda x: text(x), tweets), codes))