import tweepy

from credentials import *
keys = Keys()
auth = tweepy.OAuthHandler(keys.APIKey, keys.APIsecret)
set=set()
list = []
auth.set_access_token(keys.accessToken, keys.accessSecretToken)
api = tweepy.API(auth)
trends_place = api.trends_available()


print("---------------------")
# 2367105
count = 0

#Not the most feasible way to do it
for a in range(0,3):
    try:
        #get the popular places from trends_available
        trend = trends_place[a]
        print(trend)
        print("City:", trend["name"])
        print("Country:", trend["country"])
        print("Woeid:", trend["woeid"])
        #Find the treny topics in this location
        trend_topics = api.trends_place(id=trend["woeid"])
        topics = trend_topics[0]
        all_topics = topics["trends"]
        #Extract the name in order to use it as the query parameter.

        for top in all_topics:
            name = top["name"]
            #Avoid searching the same topic by keeping track in a set
            if name not in set:
                set.add(name)
                #Do a twitter search to find the most popular tweet regarding this topic
                search = api.search(q=name, count="1", result_type="popular", tweet_mode="extended", lang="en")
                for query in search:
                    #Extract the text, likes and retweet and add to a simple list for now
                    text=(query.full_text)
                    likes=(query.favorite_count)
                    retweet_count=(query.retweet_count)
                    list.append((text,likes,retweet_count))
    except TweepError:
        print("error")


    print(list)
    count += 1
print("count:", count)



# Portland

# trends = api.trends_closest(lat="27.88168", long="-97.31916")

# print(trends, "\n\n")



#search = api.search(q="vma", count="2", result_type="popular", tweet_mode="extended", lang="en")



# public_tweets = api.home_timeline()

# print(api.rate_limit_status())

# print("\n\n--------------\n\n")

# print(search)

print("\n\n--------------\n\n")
#to get likes query.favorite_count
#to get retweets query.retweet_count
for query in search:

    #print(query)

    print("\n")
