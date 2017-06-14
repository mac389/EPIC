import ast, gensim
from gensim import corpora 

tweets = map(ast.literal_eval,
			open('../../data/aids-test2.json','rb').read().splitlines())

texts = [tweet['text'] for tweet in tweets]



dictionary = corpora.Dictionary(texts)
corpus = [dictionary.doc2bow(text) 
                for text in texts]

lsi = gensim.models.lsimodel.LsiModel(corpus=corpus,
id2word=dictionary, num_topics=400)

lsi.print_topics(2)