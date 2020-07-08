import requests
import json
import time
from requests_oauthlib import OAuth1Session

consumer_key = "bIykEnQ31DuA4rRMOIHeiw"
consumer_secret = "wU14CMsjOan7XvZCxKYissclx1CYmYmQAILHRhFE"
access_key = "1403937170-uVXWEuzrUnMHFYmFDIyhsJWkc0I1B5Rx9OhxVXy"
access_secret = "GuEoUMBWrfPXLQgbGR90EW4BuPwc6cnAhmlKGOnDpU"

twitter = OAuth1Session('',client_secret='',resource_owner_key='',resource_owner_secret='')


url = 'https://userstream.twitter.com/1.1/user.json'
r = twitter.get(url)
data = json.loads(r.text)
print(data)