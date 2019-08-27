import tweepy
from credentials import *

keys = Keys()

auth = tweepy.OAuthHandler(keys.APIKey, keys.APIsecret)
auth.set_access_token(keys.accessToken, keys.accessSecretToken)

api = tweepy.API(auth)

trends_place = api.trends_available()
print(trends_place)
print()
print("---------------------")
# 2367105
count = 0
for trend in trends_place:
    print(trend)
    print("City:", trend["name"])
    print("Country:", trend["country"])
    print("Woeid:", trend["woeid"])
    print()
    count += 1

print("count:", count)

# Portland
# trends = api.trends_closest(lat="27.88168", long="-97.31916")
# print(trends, "\n\n")

search = api.search(q="hello", count="2", result_type="popular", tweet_mode="extended", lang="en")

# public_tweets = api.home_timeline()
# print(api.rate_limit_status())
# print("\n\n--------------\n\n")
# print(search)
print("\n\n--------------\n\n")
for query in search:
    print(query.full_text)
    print("\n")