import json, ast, itertools
from collections import Counter
from pprint import pprint 
tweets = open('../../data/aids-test2.json').read().splitlines()

#AST

#For-loop
formatted_tweets = []
for tweet in tweets:
	formatted_tweets.append(ast.literal_eval(tweet))

print formatted_tweets

#List comprehension
f_tweets = [ast.literal_eval(tweet) 
				for tweet in tweets]

texts = [tweet['text'] for tweet in f_tweets]

entities = [[word for word in text.split()
				if '@' in word] 
			for text in texts]

text_only = []
for i,text in enumerate(texts):
	text_only.append([word for word in text.split()
						if word not in entities[i]])

print text_only
x = list(itertools.chain.from_iterable(text_only))
z = dict(Counter(x))
pprint(z)
'''
for entity_list,text in zip(entities,texts):
	text_only.append([word for word in text.split()
					if word not in entity_list])
'''
''
#json.dump(f_tweets,open('test.json','wb'))
#JSON
'''
tweets = [json.loads(json.dumps(tweet)) for tweet in tweets]
print tweets

json.dump(tweets,open('test.json','wb'))

dct = json.load(open('test.json','rb'))
'''