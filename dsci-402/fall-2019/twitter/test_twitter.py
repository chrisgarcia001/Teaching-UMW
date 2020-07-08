from twitter_util import *
from sentiment import *

texts = read_texts("twitter_data/adele.json")

# n = 100
# for i in range(n):
	# print(texts[i])

codes = get_sentiment_codes("../util-data-files/AFINN-111.txt")
#print(codes)

trump = read_texts("twitter_data/trump.json")
hillary = read_texts("twitter_data/hillary.json")

print("\n---TRUMP---")
for t in trump[:10]:
	print(t, sentiment_score(codes, t))
	
print("\n---HILLARY---")
for t in hillary[:10]:
	print(t, sentiment_score(codes, t))

print("\n---LOCATIONS ON ADELE---")
adele = read_tweets("twitter_data/adele.json")	
for t in adele[:40]:
	print(text(t, ['user', 'location']))
	