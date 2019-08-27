import tweepy
from credentials import *

keys = Keys()

import tweepy

auth = tweepy.OAuthHandler(keys.APIKey, keys.APIsecret)
auth.set_access_token(keys.accessToken, keys.accessSecretToken)

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)