# -*- coding: utf-8 -*-
import nltk, re 
from autocorrect import spell

sentence = '''I wasnt able to find any indication that the 4,5-dimethoxy-2-substituted-phenethylamines have been explored pharmacologicall. Anyone know if they have?  Any guesses at potency or effect? -say if they were haloginated in the second position.
Thank you.
Some of these aren't exact subsitution patterns but I think they are relevant to your inquiry.
Ya, these are probably useful for comparison, but are  all isopropylamines.
The reasoning with this avenue (exploring 4,5-dimethoxy-2-halogenated-phenethylamines) is that when the 4th position of TMA-2 is subsituted with a halogen, potency is increased by an order of magnitude.  So what would happen if the change were at the second position (I don't of course expect these modifications are comprable)?  Perhaps 2-Br-4,5-MDA indicates that the above subsitution avenue would not be rewarding (350+mg for an amphetamine is not good).  Also when mescaline is rearranged to TMPEA, the potancy is not increased but the richness of the effects are diminished.  But yet, 2-cb is quite potent and with pleasurable effects- so couldn't it be good and some what potent- if only in theory?'''

#Figure out terminals
cList = {
  "ain't": "am not",
  "aren't": "are not",
  "can't": "cannot",
  "can't've": "cannot have",
  "'cause": "because",
  "could've": "could have",
  "couldn't": "could not",
  "couldn't've": "could not have",
  "didn't": "did not",
  "doesn't": "does not",
  "don't": "do not",
  "hadn't": "had not",
  "hadn't've": "had not have",
  "hasn't": "has not",
  "haven't": "have not",
  "he'd": "he would",
  "he'd've": "he would have",
  "he'll": "he will",
  "he'll've": "he will have",
  "he's": "he is",
  "how'd": "how did",
  "how'd'y": "how do you",
  "how'll": "how will",
  "how's": "how is",
  "I'd": "I would",
  "I'd've": "I would have",
  "I'll": "I will",
  "I'll've": "I will have",
  "I'm": "I am",
  "I've": "I have",
  "isn't": "is not",
  "it'd": "it had",
  "it'd've": "it would have",
  "it'll": "it will",
  "it'll've": "it will have",
  "it's": "it is",
  "let's": "let us",
  "ma'am": "madam",
  "mayn't": "may not",
  "might've": "might have",
  "mightn't": "might not",
  "mightn't've": "might not have",
  "must've": "must have",
  "mustn't": "must not",
  "mustn't've": "must not have",
  "needn't": "need not",
  "needn't've": "need not have",
  "o'clock": "of the clock",
  "oughtn't": "ought not",
  "oughtn't've": "ought not have",
  "shan't": "shall not",
  "sha'n't": "shall not",
  "shan't've": "shall not have",
  "she'd": "she would",
  "she'd've": "she would have",
  "she'll": "she will",
  "she'll've": "she will have",
  "she's": "she is",
  "should've": "should have",
  "shouldn't": "should not",
  "shouldn't've": "should not have",
  "so've": "so have",
  "so's": "so is",
  "that'd": "that would",
  "that'd've": "that would have",
  "that's": "that is",
  "there'd": "there had",
  "there'd've": "there would have",
  "there's": "there is",
  "they'd": "they would",
  "they'd've": "they would have",
  "they'll": "they will",
  "they'll've": "they will have",
  "they're": "they are",
  "they've": "they have",
  "to've": "to have",
  "wasn't": "was not",
  "wasnt":"was not",
  "we'd": "we had",
  "we'd've": "we would have",
  "we'll": "we will",
  "we'll've": "we will have",
  "we're": "we are",
  "we've": "we have",
  "weren't": "were not",
  "what'll": "what will",
  "what'll've": "what will have",
  "what're": "what are",
  "what's": "what is",
  "what've": "what have",
  "when's": "when is",
  "when've": "when have",
  "where'd": "where did",
  "where's": "where is",
  "where've": "where have",
  "who'll": "who will",
  "who'll've": "who will have",
  "who's": "who is",
  "who've": "who have",
  "why's": "why is",
  "why've": "why have",
  "will've": "will have",
  "won't": "will not",
  "won't've": "will not have",
  "would've": "would have",
  "wouldn't": "would not",
  "wouldn't've": "would not have",
  "y'all": "you all",
  "y'alls": "you alls",
  "y'all'd": "you all would",
  "y'all'd've": "you all would have",
  "y'all're": "you all are",
  "y'all've": "you all have",
  "you'd": "you had",
  "you'd've": "you would have",
  "you'll": "you you will",
  "you'll've": "you you will have",
  "you're": "you are",
  "you've": "you have"
}

c_re = re.compile('(%s)' % '|'.join(cList.keys()))

def expandContractions(text, c_re=c_re):
    def replace(match):
        return cList[match.group(0)]
    return c_re.sub(replace, text)

patterns = [
    (r'.*ing$', 'VBG'), # gerunds
    (r'.*ed$', 'VBD'), # simple past
    (r'.*es$', 'VBZ'), # 3rd singular present
    (r'.*ould$', 'MD'), # modals
    (r'.*\'s$', 'NN$'), # possessive nouns
    (r'.*s$', 'NNS') # plural nouns
 ]

 # remove annoying characters
chars = {
    '\xc2\x82' : ',',        # High code comma
    '\xc2\x84' : ',,',       # High code double comma
    '\xc2\x85' : '...',      # Tripple dot
    '\xc2\x88' : '^',        # High carat
    '\xc2\x91' : '\x27',     # Forward single quote
    '\xc2\x92' : '\x27',     # Reverse single quote
    '\xc2\x93' : '\x22',     # Forward double quote
    '\xc2\x94' : '\x22',     # Reverse double quote
    '\xc2\x95' : ' ',
    '\xc2\x96' : '-',        # High hyphen
    '\xc2\x97' : '--',       # Double hyphen
    '\xc2\x99' : ' ',
    '\xc2\xa0' : ' ',
    '\xc2\xa6' : '|',        # Split vertical bar
    '\xc2\xab' : '<<',       # Double less than
    '\xc2\xbb' : '>>',       # Double greater than
    '\xc2\xbc' : '1/4',      # one quarter
    '\xc2\xbd' : '1/2',      # one half
    '\xc2\xbe' : '3/4',      # three quarters
    '\xca\xbf' : '\x27',     # c-single quote
    '\xcc\xa8' : '',         # modifier - under curve
    '\xcc\xb1' : ''          # modifier - under line
}
def replace_chars(match):
    char = match.group(0)
    return chars[char]


sentence = re.sub('(' + '|'.join(chars.keys()) + ')', replace_chars, sentence)
sentence = nltk.word_tokenize(expandContractions(sentence))
sentence = map(spell,sentence)

tagged =  nltk.pos_tag(sentence)

'''
tags = {'N':"noun",'V':"verb",'I':"preposition",'J':"adjective",'R':"adverb",'D':'determiner'}
for tag,name in tags.items():
	print '%s: %s'%(name, "' | '".join([tup[0] for tup in tagged if tup[-1].startswith(tag)]))
'''

"""
[('indication', 'NN'), ('4,5-dimethoxy-2-substituted-phenethylamines', 'NNS'), ('Anyone', 'NN'), ('guesses', 'NNS'), 
('potency', 'NN'), ('effect', 'NN'), ('position', 'NN'), ('Thank', 'NNP'), ('substitution', 'NN'), ('patterns', 'NNS'), 
('inquiry', 'NN'), ('comparison', 'NN'), ('reasoning', 'NN'), ('avenue', 'NN'), ('position', 'NN'), ('TMA-2', 'NNP'), 
('halogen', 'NN'), ('potency', 'NN'), ('order', 'NN'), ('magnitude', 'NN'), ('So', 'NNP'), ('change', 'NN'), 
('position', 'NN'), ('course', 'NN'), ('modifications', 'NNS'), ('indicates', 'NNS'), ('substitution', 'NN'), 
('avenue', 'NN'), ('amphetamine', 'NN'), ('mescaline', 'NN'), ('potency', 'NN'), ('richness', 'NN'), ('effects', 'NNS'), 
('effects', 'NNS'), ('potent', 'NN'), ('theory', 'NN')]

"""

grammar = nltk.CFG.fromstring("""
	S  -> NP VP
	VP -> V
	VP -> ADV V
	VP -> V ADV
	NP -> NP PP
	PP -> PREP N
	PP -> PREP Det N
	NP -> N
	NP -> Det N
	NP -> Det ADJ N
	NP -> ADJ N
	PREP -> 'that' | 'pharmacological' | 'if' | 'at' | 'if' | 'in' | 'of' | 'for' | 'with' | 'that' | 'of' | 'with' | 'by' | 'of' | 'if' | 'at' | 'of' | 'that' | 'for' | 'of' | 'with' | 'if' | 'in'
	Det -> any' | 'the' | 'a' | 'a' | 'a' | 'the' | 'a' | 'a' | 'Some' | 'these' | 'a' | 'a' | 'these' | 'a' | 'all' | 'a' | 'The' | 'this' | 'a' | 'a' | 'the' | 'a' | 'a' | 'an' | 'a' | 'the' | 'the' | 'a' | 'these' | 'a' | 'a' | 'the' | 'a' | 'an' | 'a' | 'a' | 'a' | 'the' | 'the' | 'the' | 'a' | 'a' | 'some' | 'a
	V -> 'was' | 'find' | 'have' | 'been' | 'explored' | 'know' | 'have' | 'say' | 'were' | 'halogenated' | 'are' | 'think' | 'are' | 'are' | 'are' | 'isopropylamine' | 'exploring' | 'is' | 'is' | 'substituted' | 'is' | 'increased' | 'happen' | 'were' | 'do' | 'expect' | 'are' | 'be' | 'rewarding' | 'is' | 'is' | 'rearranged' | 'TEA' | 'is' | 'increased' | 'are' | 'diminished' | 'is' | 'be'
	N -> 'indication' | '4,5-dimethoxy-2-substituted-phenethylamines' | 'Anyone' | 'guesses' | 'potency' | 'effect' | 'position' | 'Thank' | 'substitution' | 'patterns' | 'inquiry' | 'comparison' | 'reasoning' | 'avenue' | 'position' | 'TMA-2' | 'halogen' | 'potency' | 'order' | 'magnitude' | 'So' | 'change' | 'position' | 'course' | 'modifications' | 'indicates' | 'substitution' | 'avenue' | 'amphetamine' | 'mescaline' | 'potency' | 'richness' | 'effects' | 'effects' | 'potent' | 'theory'
	ADV -> 'not' | 'not' | 'probably' | 'not' | 'Perhaps' | 'not' | 'not' | 'Also' | 'not' | 'yet' | 'so' | 'not' | 'only'
	ADJ -> 'able' | 'Any' | 'second' | 'exact' | 'relevant' | 'useful' | '4,5-dimethoxy-2-halogenated-phenethylamines' | 'th' | 'second' | 'comparable' | '2-Br-4,5-MDA' | 'above' | 'good' | '2-cb' | 'quite' | 'potent' | 'pleasurable' | 'good'
	""")

rd_parser = nltk.RecursiveDescentParser(grammar, trace=2)
for p in rd_parser.parse(sentence):
      print p