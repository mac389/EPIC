import ast, nltk, itertools
from collections import Counter
from pprint import pprint 
from nltk.corpus import wordnet
from langdetect import detect

stopwords = open('../../data/stopwords','rb').read().splitlines()

def process_tweets(tweet_text):
	return process_text(tweet_text,
						markers_of_special_tokens=['@','#'])

def process_text(tweet_text, allowed_langs=['en'],
				 markers_of_special_tokens=[]):

	if detect(tweet_text) in allowed_langs:
		text = ' '.join([token for token in tweet_text.split()
				if not any([token.startswith(markers_of_special_token) 
			for markers_of_special_token in markers_of_special_tokens])])	

		lmtzr = nltk.stem.WordNetLemmatizer()

		return ' '.join([lmtzr.lemmatize(word,get_wordnet_pos(tag))
				for word,tag in nltk.pos_tag(nltk.word_tokenize(text))]).encode('utf-8') 

	else:
		return None
	'''
			   tweet 1             tweet 2
		   [lemma lemma lemma]    [lemma lemma lemma]

			[lemma lemma lemma lemma lemma lemma ]
 
		  {"tweet 1":[lemma lemma lemma],
		   "tweet 2: [lemma lemma lemma]"}

	'''
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

def extract_by_character(maker_character,text):
	#Assumes tweets are passed as list of strings
	return [word for word in text.split()
					if maker_character in word]
	'''
	return [word for word in text.split()
				if word.startswith(maker_character)]
	'''
def extract_entities(text):
	return extract_by_character('@',text)

def extract_hashtags(text):
	return extract_by_character('#',text)

def extract_urls(text):
	return extract_by_character('https://',text)

def save_special_items(moniker,list_of_lists):
	with open('../../data/%s.txt'%moniker,'wb') as outfile:
		for lst in list_of_lists:
			print>>outfile, ' '.join(lst).encode('utf-8')

def save_entities(list_of_lists):
	return save_special_items('entities',list_of_lists)

def save_hashtags(list_of_lists):
	return save_special_items('hashtags',list_of_lists)