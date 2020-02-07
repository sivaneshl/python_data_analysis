import nltk

# part of speech tagging
text11 = "Children shouldn't drink a sugary drink before bed."
text13 = nltk.word_tokenize(text11)
pos_text13 = nltk.pos_tag(text13)
print(pos_text13)

text14 = nltk.word_tokenize("Visiting aunts can be a nuisance")
print(nltk.pos_tag(text14))

# parsing sentence structure
text15 = nltk.word_tokenize("Alice loves Bob")
grammar = nltk.CFG.fromstring('''
S -> NP VP
VP -> V NP
NP -> 'Alice' | 'Bob'
V -> 'loves'
''')
parser = nltk.ChartParser(grammar)
trees = parser.parse_all(text15)
for tree in trees:
    print(tree)

# ambiguity in parsing
text16 = nltk.word_tokenize("I saw the man with a telescope")
grammar1 = nltk.data.load('mygrammar1.cfg')
parser = nltk.ChartParser(grammar1)
trees = parser.parse_all(text16)
for tree in trees:
    print(tree)

# treebank
from nltk.corpus import treebank
text17 = treebank.parsed_sents('wsj_0001.mrg')[0]
print(text17)

# ambiguity
text18 = nltk.word_tokenize("The old man the boat")
print(nltk.pos_tag(text18))

text19 = nltk.word_tokenize("Colorless green ideas sleep furiously")
print(nltk.pos_tag(text19))
