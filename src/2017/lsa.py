import ast, gensim
from gensim import corpora 

texts = [line.split() for line in 
			open('../../data/processed.txt','rb').read().splitlines()]

dictionary = corpora.Dictionary(texts)
corpus = [dictionary.doc2bow(text) 
                for text in texts]

lsi = gensim.models.lsimodel.LsiModel(corpus=corpus,
id2word=dictionary, num_topics=400)

lsi.print_topics(2)