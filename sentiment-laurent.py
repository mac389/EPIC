import nltk, tweepy, json, io

pos_tweets = [('I love this car', 'positive'),
              ('This view is amazing', 'positive'),
              ('I feel great this morning', 'positive'),
              ('I am so excited about the concert', 'positive'),
              ('He is my best friend', 'positive'),
              ('She is excellent', 'positive'),
              ('We are really nice', 'positive'),
              ('We are very wonderful', 'positive')]

neg_tweets = [('I do not like this car', 'negative'),
              ('This view is horrible', 'negative'),
              ('I feel tired this morning', 'negative'),
              ('I am not looking forward to the concert', 'negative'),
              ('He is my enemy', 'negative'),
              ('She is so awful and terrible', 'negative'),
              ('We are really cruel and mean', 'negative'),
              ('We are very evil and nasty', 'negative')]

tweets = []
for (words, sentiment) in pos_tweets + neg_tweets:
    words_filtered = [e.lower() for e in words.split() if len(e) >= 3] 
    tweets.append((words_filtered, sentiment))
    

#print tweets   

    
def get_words_in_tweets(tweets):
    all_words = []
    for (words, sentiment) in tweets:
        all_words.extend(words)
    return all_words    
    
    
def get_word_features(wordlist):
    wordlist = nltk.FreqDist(wordlist)
    word_features = wordlist.keys()
    return word_features

word_features = get_word_features(get_words_in_tweets(tweets))

#To make the classifier..
#The list of word features need to be extracted from the tweets. 
#It is a list with every distinct words ordered by frequency of appearance. We use word_features to get the list plus the two helper functions, get_word_Features and get_words_in_tweets

#print word_features


def extract_features(document):
    document_words = set(document)
    features = {}
    for word in word_features:
        features['contains(%s)' % word] = (word in document_words)
    return features

training_set = nltk.classify.apply_features(extract_features, tweets)

#The variable 'training_set' contains the labeled feature sets.
#It is a list of tuples which each tuple containing the feature dictionary and the sentiment string for each tweet. The sentiment string is also called 'label'.
#so for the first tweet you get love,this,car as true and every other word as false ... for the second tweet it's  this, view, amazing as true and everything else is false 

#print training_set



classifier = nltk.NaiveBayesClassifier.train(training_set)

tweet = 'Larry is my enemy'

print 'Tweet: %s ... has a %s sentiment'  % (tweet, classifier.classify(extract_features(tweet.split())))

print '\n'

tweet = 'Larry is my nemesis'

print 'Tweet: %s ... has a %s sentiment'  % (tweet, classifier.classify(extract_features(tweet.split())))