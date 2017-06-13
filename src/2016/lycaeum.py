import pandas as pd 

df = pd.read_json('./db.json').transpose()
corpus = df['text'].tolist()

#Length of list
print len(corpus)

#What does the first entry look like?
print corpus[0]

print ' '.join(df['text'].tolist()).split().count('flush')

import json

contractions = json.load(open('contractions.json','rb'))

for contraction,expansion in contractions.iteritems():
    #if / ; in expansion replace that expansion with 
        #expansion split on those characters
    if ';' in expansion:
        expansion = expansion.replace(';','/')
    if '/' in expansion:
        expansion = expansion.split('/')[0]

    contractions[contraction] = expansion

'''
def cleanse(text):
    #Deal with contractions
    corpus = [text.replace(contraction,expansion) 
                if contraction in text else text
                for text in corpus 
                for contraction,expansion in contractions.iteritems()]
    #Remove punctuation
    #Remove stopwords
    #Tokenize
    #Lemmatize
'''

corpus = df['processed_text'].tolist()
from collections import Counter 
import itertools 

words,freqs = zip(*sorted(dict(Counter(itertools.chain.from_iterable(corpus))).items(), 
                key=lambda item:item[1],reverse=True))

'''
import matplotlib.pyplot as plt 
cutoff = 20
fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(freqs[:cutoff],'k--')
ax.set_xticks(range(cutoff))
ax.set_xticklabels(words[:cutoff],rotation='vertical')
plt.tight_layout()
plt.savefig('lycaeum.png')
'''

from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np 
vectorizer = TfidfVectorizer(min_df=1)
response = vectorizer.fit_transform([' '.join(text) for text in corpus])

feature_array = vectorizer.get_feature_names()
tfidf_sorting = np.argsort(response.toarray()).flatten()[::-1]

n = 20
top_n = feature_array[tfidf_sorting][:n]