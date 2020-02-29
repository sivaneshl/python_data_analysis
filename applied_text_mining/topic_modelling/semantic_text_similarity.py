import nltk
from nltk.corpus import wordnet as wn

deer = wn.synset('deer.n.01')
elk = wn.synset('elk.n.01')
horse = wn.synset('horse.n.01')

# path similarity
print('Path Similarity - deer-elk:', deer.path_similarity(elk))
print('Path Similarity - deer-horse:', deer.path_similarity(horse))

# lin similarity
from nltk.corpus import wordnet_ic
brown_ic = wordnet_ic.ic('ic-brown.dat')
print('Lin Similarity - deer-elk:', deer.lin_similarity(elk, brown_ic))
print('Lin Similarity - deer-horse:', deer.lin_similarity(horse, brown_ic))

# collocations and distributional similarity
from nltk.collocations import *
from nltk.book import *
bigram_measures = nltk.collocations.BigramAssocMeasures()
finder = BigramCollocationFinder.from_words(text1)
print(finder.nbest(bigram_measures.pmi, 10))
print(finder.apply_freq_filter(10))  # - restrict words that do not occur 10 times in corpus
