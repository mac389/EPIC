import pandas as pd 
import itertools

import matplotlib.pyplot as plt 

from awesome_print import ap 
from string import punctuation
from collections import Counter 

url = "https://data.cityofnewyork.us/resource/xx67-kt59.json"
df = pd.read_json(url)

corpus = df['violation_description'].tolist()

from nltk import pos_tag
from nltk.corpus import stopwords
from nltk.corpus import wordnet as wn
from nltk.stem.wordnet import WordNetLemmatizer
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
        return treebank_tag

def word_tokenize(lst):
    our_emoticons = []
    everything_else = []
    for token in lst:
        if token in emoticons:
            our_emoticons.append((token,'EMOTICON'))
        else:
            everything_else.append(token)
    tagged = nltk.pos_tag(everything_else)
    tagged.extend(our_emoticons)
    return tagged

lmtzr = WordNetLemmatizer()
our_stopwords = stopwords.words('english')

#get rid of and/or

corpus = [text.replace('/',' ').replace("'s",'').replace("n't"," not").replace("-","") 
            for text in corpus
            if type(text) == str or
               type(text) == unicode]


tokenized = [pos_tag(word_tokenize(phrase.lower()))
                for phrase in corpus]

lmtzr.lemmatize("bob")

fully_processed = [lmtzr.lemmatize(token,pos=get_wordnet_pos(pos)) 
                    if get_wordnet_pos(pos) in ['J','V','N','R']
                    else lmtzr.lemmatize(token) 
                for token,pos in itertools.chain.from_iterable(tokenized)
                if token not in punctuation 
                and token not in our_stopwords]

emoticons = [":-)"]


test_sentence = "I like bob :-)."
for emoticon in emoticons: 
    emoticons_in_sentence = []
    if emoticon in test_sentence:
        emoticons_in_sentence.append(emoticon)
        test_sentence = test_sentence.replace(emoticon,"")
tt = [word for word in nltk.word_tokenize(test_sentence) 
            if word not in punctuation]
tt.extend(emoticons_in_sentence)      

print word_tokenize(tt)

all_words = list(set(dict(Counter(fully_processed)).keys()))

words,freqs = zip(*sorted(dict(Counter(fully_processed)).items(),
        key = lambda item:item[1],
        reverse=True))
        
import numpy as np 

data = np.array([[sum([1 for document in corpus if 
                        one in document and two in document]) 
                for one in words[:20]] 
                for two in words[:20]])

fig = plt.figure()
ax = fig.add_subplot(111)
cax = ax.imshow(data,interpolation='nearest',aspect='auto',cmap=plt.cm.bone_r)
plt.colorbar(cax)
plt.tight_layout()
plt.savefig('co-occurence_slim.png')
cutoff = 20

zip([1,2],[3,4])

words,freqs = zip(*sorted(dict(Counter(fully_processed)).items(),
        key = lambda item:item[1],
        reverse=True))
        
fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(freqs[:cutoff],'k--')
ax.set_xticks(range(cutoff))
ax.set_xticklabels(words[:cutoff],rotation='vertical')
plt.tight_layout()
plt.savefig('ffg.png')