import tweepy
from credentials import *

keys = Keys()

import tweepy

auth = tweepy.OAuthHandler(keys.APIKey, keys.APIsecret)
auth.set_access_token(keys.accessToken, keys.accessSecretToken)

api = tweepy.API(auth)

search = api.search(q="hello", rpp="3", count="2", result_type="popular", tweet_mode="extended")

# public_tweets = api.home_timeline()
# print(api.rate_limit_status())
print("\n\n--------------\n\n")
print(search)
print("\n\n--------------\n\n")
for query in search:
    print(query.full_text)
    print("\n")