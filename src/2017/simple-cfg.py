import nltk

sentence = "I could not find any indication that the 4,5-dimethoxy-2-substituted-phenethylamines"


grammar = nltk.CFG.fromstring("""
	S  -> NP VP
	NP -> Det N
	NP -> N 
	VP -> Mod Neg V NP
	VP -> Mod V NP
	VP -> Mod V
	VP -> Neg V NP
	VP -> Neg V 
	VP -> Mod Neg V
	Mod -> 'could'
	Neg -> 'not'
	V -> 'find'
	Det -> 'any'
	N -> 'I' | 'indication'
	""")

rd_parser = nltk.RecursiveDescentParser(grammar, trace=2)
for p in rd_parser.parse(sentence.split()):
      print dir(p)
      p.draw()