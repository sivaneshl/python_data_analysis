import nltk
import nltk.corpus
# nltk.download()

from nltk.book import *

print(text1)

print(sents())

print(sent1)

# counting vocabulary of words
print(text7)
print(sent7)
print(len(sent7))
print(len(text7))
print(len(set(text7)))  # unique words
print(list(set(text7))[:10])    # first 10 words

# frequency of words
dist = FreqDist(text7)
print(len(dist))

# first 10 words
vocab1 = dist.keys()
print(list(vocab1)[:10])

# how many times a word occurs
print(dist['board'])

# frequent words
frequentwords = [w for w in list(dist.keys()) if len(w)>5 and dist[w]>100]
print(frequentwords)

# normalizing and stemming
input1 = 'List listed lists listing listings'
words1 = input1.lower().split(' ')
porter = nltk.PorterStemmer()   # find the root of the word
print([porter.stem(t) for t in words1])

# lemmatization
udhr = nltk.corpus.udhr.words('English-Latin1')
print(udhr[:20])
print(porter.stem(t) for t in udhr[:20])    # stemming gives meaningless words
# lemmatization = stemming but resulting words are valid words
WNLemma = nltk.WordNetLemmatizer()
print([WNLemma.lemmatize(t) for t in udhr[:20]])

# tokeniztion
text11 = "Children shouldn't drink a sugary drink before bed."
print(text11.split(' '))
print(nltk.word_tokenize(text11))

# sentence splitting
text12 = "This is the first sentence. A gallon of milk in the U.S. costs $2.99. Is this the third sentence? Yes, it is!"
sentences = nltk.sent_tokenize(text12)
print(sentences)
print(len(sentences))

