import ast 

tweets = map(ast.literal_eval,
			open('../../data/aids-test2.json','rb').read().splitlines())

coordinates = [tweet['geo'] for tweet in tweets]
print coordinates