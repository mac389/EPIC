import ast
from collections import Counter
from pprint import pprint 

#Load tweets 
tweets = open('../../data/aids-test2.json','rb').read().splitlines()
'''
  Tweets is a list of strings. 
  Each string is a JSON object
'''

#Convert strings to JSON using ast
tweets = map(ast.literal_eval,tweets)
print tweets

'''
#Alternates 
tweets = [ast.literal_eval(tweet) for tweet in tweets]

#In explicit for-loop
formatted_tweets = []
for tweet in tweets:
	formatted_tweets.append(ast.literal_eval(tweet))

print formatted_tweets
'''

texts = [tweet['text'] for tweet in tweets]

def extract_by_character(maker_character,text):
	#Assumes tweets are passed as list of strings
	return [word for word in text.split()]
					if maker_character in word]
					
def extract_entities(text):
	return extract_by_character('@',text)

def extract_hashtags(text):
	return extract_by_character('#',text)

entities = map(extract_entities,texts)
#Equivalent to
# entities = [extract_entities[text] for text in texts]
hashtags = map(extract_hashtags,texts)
#Equivalent to
# hashtags = [extract_hashtags[text] for text in texts]

text_only = []
for i,text in enumerate(texts):
	text_only.append([word for word in text.split()
						if word not in entities[i]
						and if word not in hashtags[i]])


'''
#Alternate
 for text,hashtag,entity_list in zip(texts, hashtags, entities):
 	exluded = hashtags + entities
 	text_only.append([word for word in text.split() 	
 						if word not in exluded])
'''

#Flatten list of list of tokens to list of tokens
x = list(itertools.chain.from_iterable(text_only))

#Count tokens
z = dict(Counter(x))
pprint(z)