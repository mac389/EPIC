import json, os, carmen, ast, itertools 
DATA_PATH = '../../data'

filenames = [filename for filename in os.listdir(DATA_PATH)
				if 'schizophrenia' in filename]


tweets = []
for filename in filenames:
	full_filename = os.path.join(DATA_PATH,filename)
	tweets.append(open(full_filename,'rb').read().splitlines())

tweets = [map(ast.literal_eval,tweet_list) for tweet_list in tweets]

resolver = carmen.get_resolver()
resolver.load_locations()

for tweet in itertools.chain.from_iterable(tweets):
	print '_________________'
	print tweet['text']
	print 'Location: ',resolver.resolve_tweet(tweet)
	print '_________________'