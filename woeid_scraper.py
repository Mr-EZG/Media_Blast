import tweepy
from credentials import *
from DataBase import *
from Utils import *

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
l_of_dict = []
things_to_store = ["country", "name", "woeid"]
for trend in trends_place:
    d = {}
    for thing in things_to_store:
        d[thing] = trend[thing]
    l_of_dict.append(d)
    count += 1


print("count:", count)
db = DataBase(config.woeid_dir, things_to_store)

db.reset()

for row in l_of_dict:
    db.update_row(row)

db.save()