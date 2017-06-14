import ast, nltk, itertools
from collections import Counter
from pprint import pprint 
from nltk.corpus import wordnet

def get_wordnet_pos(treebank_tag):

    if treebank_tag.startswith('J'):
        return wordnet.ADJ
    elif treebank_tag.startswith('V'):
        return wordnet.VERB
    elif treebank_tag.startswith('N'):
        return wordnet.NOUN
    elif treebank_tag.startswith('R'):
        return wordnet.ADV
    else:
        return wordnet.NOUN
#Load tweets 
tweets = open('../../data/aids-test2.json','rb').read().splitlines()
stopwords = open('../../data/stopwords','rb').read().splitlines()
'''
  Tweets is a list of strings. 
  Each string is a JSON object
'''

#Convert strings to JSON using ast
tweets = map(ast.literal_eval,tweets)
#print tweets

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
	return [word for word in text.split()
					if maker_character in word]
					
def extract_entities(text):
	return extract_by_character('@',text)

def extract_hashtags(text):
	return extract_by_character('#',text)

def save_special_items(moniker,list_of_lists):
	with open('../../data/%s.txt','wb') as outfile:
		for lst in list_of_lists:
			print>>outfile, ' '.join(lst).encode('utf-8')

def save_entities(list_of_lists):
	return save_special_items('entities',list_of_lists)

def save_hashtags(list_of_lists):
	return save_special_items('hashtags',list_of_lists)


entities = map(extract_entities,texts)
#Equivalent to
# entities = [extract_entities[text] for text in texts]

#Write entities to file
#Each line contains the entities from one tweet separated by a space
save_entities(entities)

hashtags = map(extract_hashtags,texts)
#Equivalent to
# hashtags = [extract_hashtags[text] for text in texts]

#Write, similarly, hashtags to file
save_hashtags(hashtags)

text_only = []
for i,text in enumerate(texts):
	text_only.append([word for word in text.split()
						if word not in entities[i]
						and word not in hashtags[i]])

'''
#Alternate
 for text,hashtag,entity_list in zip(texts, hashtags, entities):
 	exluded = hashtags + entities
 	text_only.append([word for word in text.split() 	
 						if word not in exluded])
'''

'''
#If bag of words
#Lemmatize
lemmatized = []
for text in text_only:
	tagged = nltk.pos_tag(text)
	for word, tag in tagged:
		lemmatized.append(nltk.stem.WordNetLemmatizer().lemmatize(word,get_wordnet_pos(tag)))
#Flatten list of list of tokens to list of tokens
x = list(itertools.chain.from_iterable(text_only))
'''

with open('../../data/processed.txt','wb') as outfile:
	for tweet in text_only:
		processed_tweet = []
		as_string = ' '.join(tweet).lower()
		for word, tag in nltk.pos_tag(nltk.word_tokenize(as_string)):
			#For better tokenizing use regular expressions
			#Control side effects
			processed_tweet.append(nltk.stem.WordNetLemmatizer().lemmatize(word,get_wordnet_pos(tag)))
		processed_tweet = [token for token in processed_tweet if token not in stopwords]
		print processed_tweet
		print>>outfile,' '.join(processed_tweet).encode('utf-8')