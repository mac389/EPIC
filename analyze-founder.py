import tweepy, io, json

from getpass import getpass

def serialize_tweepy_object(obj):
    tweet = {}
    tweet['retweet_count'] = len(api.retweets(obj.id)) #Ceiling effect because max is 100
    tweet['author-name'] = obj.author.name.encode('utf8')
    tweet['screen-name'] = obj.author.screen_name.encode('utf8')
    tweet['created-at'] = obj.created_at.strftime('%m-%d-%Y')
    tweet['text'] = obj.text.encode('utf8')
    
    text = obj.text.encode('utf8')
    words = ''.join(c if c.isalnum() else ' ' for c in text).split()

    tweet['analysis'] = {}
    tweet['analysis']['tweet_length'] = len(text) 
    tweet['analysis']['word-count'] = len(words)

    tweet['location'] = obj.user.location.encode('utf8')
    tweet['time-zone'] = obj.user.time_zone
    tweet['isGeo'] = obj.geo

    tweet['retweet_count'] = obj.retweet_count
    tweet['favorite_count'] = obj.favorite_count

    return tweet

# Consumer keys and access tokens, used for OAuth
READ = 'rb'
WRITE = 'wb'
tokens = json.load(open('tokens.json',READ))   
 
# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(tokens['consumer_key'], tokens['consumer_secret'])
auth.set_access_token(tokens['access_token'], tokens['access_token_secret'])

# Creation of the actual interface, using authentication
api = tweepy.API(auth)

user_file = open('usertimeline.json',WRITE)
user_text_file = open('usertimeline.txt','a')
user_excel_file = open('usertimeline.csv','a')
json_list = []
for tweet in tweepy.Cursor(api.user_timeline, id="ev", include_rts=False).items(10):
    tweet = serialize_tweepy_object(tweet)
    json_list.append(tweet)

    user_text_file.write(tweet['text'] + '\n')
    user_excel_file.write(str(tweet['author-name']) + '|' + tweet['text'] + '|' + str(tweet['location']) + '|' + str(tweet['retweet_count']) + '|' + str(tweet['favorite_count']) + '\n')

json.dump(json_list,user_file)

