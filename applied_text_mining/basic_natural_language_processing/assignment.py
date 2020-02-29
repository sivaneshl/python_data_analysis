import nltk
import pandas as pd
import numpy as np
from nltk.book import FreqDist
from nltk.stem import WordNetLemmatizer
from nltk.corpus import words

# If you would like to work with the raw text you can use 'moby_raw'
with open('../resources/moby.txt', 'r') as f:
    moby_raw = f.read()

# If you would like to work with the novel in nltk.Text format you can use 'text1'
moby_tokens = nltk.word_tokenize(moby_raw)
text1 = nltk.Text(moby_tokens)

# Example 1
# How many tokens (words and punctuation symbols) are in text1?
# This function should return an integer.
def example_one():
    return len(text1)

# Example 2
# How many unique tokens (unique words and punctuation) does text1 have?
# This function should return an integer.
def example_two():
    return len(set(text1))

# Example 3
# After lemmatizing the verbs, how many unique tokens does text1 have?
# This function should return an integer.
def example_three():
    lemmatizer = WordNetLemmatizer()
    lemmatized = [lemmatizer.lemmatize(w, 'v') for w in text1]
    return len(set(lemmatized))

# Question 1
# What is the lexical diversity of the given text input? (i.e. ratio of unique tokens to the total number of tokens)
# This function should return a float.
def question_one():
    total_tokens = example_one()
    unique_tokens = example_two()
    return unique_tokens / total_tokens

# Question 2
# What percentage of tokens is 'whale'or 'Whale'?
# This function should return a float.
def question_two():
    dist = FreqDist(text1)
    total_tokens = example_one()
    return 100 * ((dist['whale'] + dist['Whale']) / total_tokens)

# Question 3
# What are the 20 most frequently occurring (unique) tokens in the text? What is their frequency?
# This function should return a list of 20 tuples where each tuple is of the form (token, frequency).
# The list should be sorted in descending order of frequency.
def question_three():
    dist = FreqDist(text1)
    return dist.most_common(20)

# Question 4
# What tokens have a length of greater than 5 and frequency of more than 150?
# This function should return an alphabetically sorted list of the tokens that match the above constraints.
# To sort your list, use sorted()
def question_four():
    dist = FreqDist(text1)
    frequentwords = [w for w in list(dist.keys()) if len(w) > 5 and dist[w] > 150]
    return sorted(frequentwords)

# Question 5
# Find the longest word in text1 and that word's length.
# This function should return a tuple (longest_word, length).
def question_five():
    longest = ''
    for word in text1:
        if len(word) > len(longest):
            longest = word
    return (longest, len(longest))

# Question 6
# What unique words have a frequency of more than 2000? What is their frequency?
# "Hint: you may want to use isalpha() to check if the token is a word and not punctuation."
# This function should return a list of tuples of the form (frequency, word) sorted in descending order of frequency.
def question_six():
    dist = FreqDist(text1)
    frequentwords = [w for w in list(dist.keys()) if w.isalpha() and dist[w] > 2000]
    return sorted([(dist[w], w) for w in frequentwords], reverse=True)

# Question 7
# What is the average number of tokens per sentence?
# This function should return a float.
def question_seven():
    sentences = nltk.sent_tokenize(moby_raw)
    word_counts = [len(nltk.word_tokenize(sentence)) for sentence in sentences]
    return sum(word_counts) / len(sentences)

# Question 8
# What are the 5 most frequent parts of speech in this text? What is their frequency?
# This function should return a list of tuples of the form (part_of_speech, frequency) sorted in descending order
# of frequency.
def question_eight():
    pos_tags = nltk.pos_tag(moby_tokens)
    pos_freq = FreqDist([pos_tag for (word, pos_tag) in pos_tags])
    return pos_freq.most_common(5)



# print(example_one())
# print(example_two())
# print(example_three())
# print(question_one())
# print(question_two())
# print(question_three())
# print(question_four())
# print(question_five())
# print(question_six())
# print(question_seven())
# print(question_eight())


# Part 2 - Spelling Recommender
# For this part of the assignment you will create three different spelling recommenders, that each take a list
# of misspelled words and recommends a correctly spelled word for every word in the list.
# For every misspelled word, the recommender should find find the word in correct_spellings that has the shortest
# distance*, and starts with the same letter as the misspelled word, and return that word as a recommendation.
# *Each of the three different recommenders will use a different distance measure (outlined below).
# Each of the recommenders should provide recommendations for the three default words provided:
#     ['cormulent', 'incendenece', 'validrate'].
correct_spellings = words.words()

# Question 9
# For this recommender, your function should provide recommendations for the three default words provided above using
# the following distance metric:
# Jaccard distance on the trigrams of the two words.
# This function should return a list of length three:
# ['cormulent_reccomendation', 'incendenece_reccomendation', 'validrate_reccomendation'].
def answer_nine(entries=['cormulent', 'incendenece', 'validrate']):
    result = []
    n=3
    for entry in entries:
        words = [word for word in correct_spellings if word[0]==entry[0]]
        distances = [(nltk.jaccard_distance(set(nltk.ngrams(entry, n=n)), set(nltk.ngrams(match, n=n))),
                      match) for match in words]
        result.append(sorted(distances)[0][1])
    return result

# Question 10
# For this recommender, your function should provide recommendations for the three default words provided above
# using the following distance metric:
# Jaccard distance on the 4-grams of the two words.
# This function should return a list of length three: [
#     'cormulent_reccomendation', 'incendenece_reccomendation', 'validrate_reccomendation'].
def answer_ten(entries=['cormulent', 'incendenece', 'validrate']):
    result = []
    n=4
    for entry in entries:
        words = [word for word in correct_spellings if word[0] == entry[0]]
        distances = [(nltk.jaccard_distance(set(nltk.ngrams(entry, n=n)), set(nltk.ngrams(match, n=n))),
                      match) for match in words]
        result.append(sorted(distances)[0][1])
    return result

# Question 11
# For this recommender, your function should provide recommendations for the three default words provided above using the
# following distance metric:
# Edit distance on the two words with transpositions.
# This function should return a list of length three:
# ['cormulent_reccomendation', 'incendenece_reccomendation', 'validrate_reccomendation'].
def answer_eleven(entries=['cormulent', 'incendenece', 'validrate']):
    result = []
    for entry in entries:
        words = [word for word in correct_spellings if word[0] == entry[0]]
        distances = [(nltk.edit_distance(entry, match), match) for match in words]
        result.append(sorted(distances)[0][1])
    return result


print(answer_nine())
print(answer_ten())
print(answer_eleven())