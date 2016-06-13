import json

from textstat.textstat import textstat

filename = 'usertimeline.json'
READ = 'rb'
TEXT=1

tweets = json.load(open(filename,READ))
#Identify retweets
retweets = [word for tweet in tweets for word in tweet['text'][TEXT] if 'RT' in word]

print retweets
#identify replies

#Word count
print [tweet['analysis']['word-count'] for tweet in tweets]

#How would you do a character count?

#Lexical diversity
lex_div = lambda text: len(text.split())/float(len(set(text.split())))
print [lex_div(tweet['text'][TEXT]) for tweet in tweets]

#F-K
print [textstat.flesch_kincaid_grade(tweet['text'][TEXT]) for tweet in tweets]

#remove stopwords
print [[word for word in tweet['text'][TEXT].split() if word not in stopwords.words('english') ] for tweet in tweets]
#What's another way to filter out stopwords?
#How to handle punctuation?