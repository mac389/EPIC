import json 

from TwitterAPI import TwitterAPI

keys = json.load(open(''))
api = TwitterAPI(consumer_key, consumer_secret, access_token_key, access_token_secret)