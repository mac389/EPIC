import json, os, ast, itertools
import utils as tech 
'''
  [item, item, item]

  [[item, item, [item]],[item, item]]

''' 

DATA_PATH = '../../data'
#print os.path.join(DATA_PATH,'stopwords')

#print os.getcwd()
#print os.listdir(os.getcwd())


'''
for filename in os.listdir(DATA_PATH):
	if 'schizophrenia' in filename:
		print filename
'''
filenames = [filename for filename in os.listdir(DATA_PATH)
				if 'schizophrenia' in filename]


tweets = []
for filename in filenames:
	full_filename = os.path.join(DATA_PATH,filename)
	tweets.append(open(full_filename,'rb').read().splitlines())

tweets = [map(ast.literal_eval,tweet_list) for tweet_list in tweets]
'''

tweets = [map(ast.literal_eval(open(os.path.join(DATA_PATH,
					filename),'rb').read().splitlines()))
				for filename in filenames]
'''

tweets = list(itertools.chain.from_iterable(tweets))
tweets = map(tech.process_tweets,[tweet['text'] for tweet in tweets])

with open(os.path.join(DATA_PATH,'schizo-processed.txt'),'wb') as outfile:
	for tweet in tweets:
		print>>outfile, tweet

