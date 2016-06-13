import json

filename = 'usertimeline.json'
READ = 'rb'
tweets = json.load(open(filename,READ))

#Which hashtags were used?

TEXT=1
hashtags = [word for tweet in tweets for word in tweet['text'][TEXT].split() if '#' in word]
#print hashtags

#Which tweet is most popular? (Which tweet has the most retweets?)
retweets = sorted(tweets,key = lambda tweet: tweet['retweet_count'],reverse=True)
print retweets[0]

#Get location from tweet
locations = [tweet['location'] for tweet in tweets]
print locations