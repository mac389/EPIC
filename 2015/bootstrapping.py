import json
import numpy as np
from random import shuffle, sample

import matplotlib.pyplot as plt 

READ = 'rb'
WRITE = 'wb'

bieber = [tweet['text'].split() for tweet in json.load(open('bieber-raw-test.json',READ))]

sxsw = [tweet['text'].split() for tweet in json.load(open('sxsw-SXSW-#SXSW-#sxsw-20140308-001535.json',READ))]

shuffle(sxsw)

short_sxsw = sample(sxsw,len(bieber))

def jaccard_similarity(one,two):
	return len(set(one) & set(two))/float(len(set(one) | set(two)))

iterations = 1000

combined = bieber + short_sxsw
similarities = []
similarities.append(np.average([jaccard_similarity(a,b) for a in bieber for b in short_sxsw]))

for iteration in xrange(iterations):
	if iteration%100 == 0:
		print iteration
	n_samples = len(combined)/2

	one_idx = set(sample(xrange(len(combined)),n_samples))
	two_idx = set(xrange(len(combined))) - one_idx

	one = [combined[idx] for idx in one_idx]
	two = [combined[idx] for idx in two_idx]
	
	similarities.append(np.average([jaccard_similarity(a,b) for a in one for b in two]))

fig = plt.figure()
ax = fig.add_subplot(111)
ax.hist(similarities,bins=20,color='k')

ax.annotate('Our sample', xy=(similarities[0], 100),  xycoords='data',
            xytext=(0.2, 0.4), textcoords='axes fraction',
            arrowprops=dict(facecolor='black', shrink=0.05),
            horizontalalignment='right', verticalalignment='top',
            )
#-- Make it look nice
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.spines['left'].set_position(('outward',10))
ax.spines['bottom'].set_position(('outward',10))
ax.yaxis.set_ticks_position('left')
ax.xaxis.set_ticks_position('bottom')

#---
ax.set_ylabel('Frequency')
ax.set_xlabel('Jaccard Similarity')
plt.show()