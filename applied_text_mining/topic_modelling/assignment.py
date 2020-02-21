# Assignment 4 - Document Similarity & Topic Modelling

import pandas as pd
import numpy as np
import nltk
from nltk.corpus import wordnet as wn
from sklearn.metrics import accuracy_score

# Part 1 - Document Similarity

# For the first part of this assignment, you will complete the functions doc_to_synsets and similarity_score
# which will be used by document_path_similarity to find the path similarity between two documents.

# The following functions are provided:
# convert_tag: converts the tag given by nltk.pos_tag to a tag used by wordnet.synsets. You will need to use
# this function in doc_to_synsets.
# document_path_similarity: computes the symmetrical path similarity between two documents by finding the
# synsets in each document using doc_to_synsets, then computing similarities using similarity_score.

# You will need to finish writing the following functions:
# doc_to_synsets: returns a list of synsets in document. This function should first tokenize and part of speech
# tag the document using nltk.word_tokenize and nltk.pos_tag. Then it should find each tokens corresponding
# synset using wn.synsets(token, wordnet_tag). The first synset match should be used. If there is no match,
# that token is skipped.
# similarity_score: returns the normalized similarity score of a list of synsets (s1) onto a second list
# of synsets (s2). For each synset in s1, find the synset in s2 with the largest similarity value. Sum all of
# the largest similarity values together and normalize this value by dividing it by the number of largest
# similarity values found. Be careful with data types, which should be floats. Missing values should be ignored.
# Once doc_to_synsets and similarity_score have been completed, submit to the autograder which will run test_
# document_path_similarity to test that these functions are running correctly.
#
# Do not modify the functions convert_tag, document_path_similarity, and test_document_path_similarity.

def convert_tag(tag):
    """Convert the tag given by nltk.pos_tag to the tag used by wordnet.synsets"""

    tag_dict = {'N': 'n', 'J': 'a', 'R': 'r', 'V': 'v'}
    try:
        return tag_dict[tag[0]]
    except KeyError:
        return None


def doc_to_synsets(doc):
    """
    Returns a list of synsets in document.

    Tokenizes and tags the words in the document doc.
    Then finds the first synset for each word/tag combination.
    If a synset is not found for that combination it is skipped.

    Args:
        doc: string to be converted

    Returns:
        list of synsets

    Example:
        doc_to_synsets('Fish are nvqjp friends.')
        Out: [Synset('fish.n.01'), Synset('be.v.01'), Synset('friend.n.01')]
    """

    tokens = nltk.word_tokenize(doc)
    pos_tokens = nltk.pos_tag(tokens)
    converted_tags = [(tag[0], convert_tag(tag[1])) for tag in pos_tokens]
    retuns_synsets = [wn.synsets(x, y) for x, y in converted_tags]
    return [x[0] for x in retuns_synsets if len(x) > 0]

# print(doc_to_synsets('Fish are nvqjp friends.'))


def similarity_score(s1, s2):
    """
    Calculate the normalized similarity score of s1 onto s2

    For each synset in s1, finds the synset in s2 with the largest similarity value.
    Sum of all of the largest similarity values and normalize this value by dividing it by the
    number of largest similarity values found.

    Args:
        s1, s2: list of synsets from doc_to_synsets

    Returns:
        normalized similarity score of s1 onto s2

    Example:
        synsets1 = doc_to_synsets('I like cats')
        synsets2 = doc_to_synsets('I like dogs')
        similarity_score(synsets1, synsets2)
        Out: 0.73333333333333339
    """

    s = []
    for s1_item in s1:
        scores = [x for x in [s1_item.path_similarity(s2_item) for s2_item in s2] if x is not None]
        if scores:
            s.append(max(scores))
    return sum(s) / len(s)

    # return np.mean([np.nanmax(np.array(([x for x in [s1_synset.path_similarity(s2_synset) for s2_synset in s2] if x is not None]), dtype=np.float64))
    #        for s1_synset in s1])

    # return np.mean([max([s1_synset.path_similarity(s2_synset) for s2_synset in s2]) for s1_synset in s1])

# synsets1 = doc_to_synsets('I like cats')
# synsets2 = doc_to_synsets('I like dogs')
# print(similarity_score(synsets1, synsets2))


def document_path_similarity(doc1, doc2):
    """Finds the symmetrical similarity between doc1 and doc2"""

    synsets1 = doc_to_synsets(doc1)
    synsets2 = doc_to_synsets(doc2)

    return (similarity_score(synsets1, synsets2) + similarity_score(synsets2, synsets1)) / 2

# print(document_path_similarity('I like cats', 'I like dogs'))


# test_document_path_similarity
# Use this function to check if doc_to_synsets and similarity_score are correct.
# This function should return the similarity score as a float.
def test_document_path_similarity():
    doc1 = 'This is a function to test document_path_similarity.'
    doc2 = 'Use this function to see if your code in doc_to_synsets and similarity_score is correct!'
    return document_path_similarity(doc1, doc2)

# print(test_document_path_similarity())


# paraphrases is a DataFrame which contains the following columns: Quality, D1, and D2.
# Quality is an indicator variable which indicates if the two documents D1 and D2 are paraphrases of one another
# (1 for paraphrase, 0 for not paraphrase).
# Use this dataframe for questions most_similar_docs and label_accuracy
paraphrases = pd.read_csv('../resources/paraphrases.csv')
# print(paraphrases.head())

# most_similar_docs
# Using document_path_similarity, find the pair of documents in paraphrases which has the maximum similarity score.
# This function should return a tuple (D1, D2, similarity_score)
def most_similar_docs():
    return max([[paraphrase['D1'], paraphrase['D2'], document_path_similarity(paraphrase['D1'], paraphrase['D2'])] for index, paraphrase in paraphrases.iterrows()],
               key=lambda doc: doc[2])

# print(most_similar_docs())

# label_accuracy
# Provide labels for the twenty pairs of documents by computing the similarity for each pair using
# document_path_similarity. Let the classifier rule be that if the score is greater than 0.75, label is
# paraphrase (1), else label is not paraphrase (0). Report accuracy of the classifier using scikit-learn's
# accuracy_score.
# This function should return a float.
def label_accuracy():
    predict_label = []
    for i in range(len(paraphrases)):
        similarity = document_path_similarity(paraphrases['D1'][i], paraphrases['D2'][i])
        if similarity > 0.75:
            predict_label.append(1)
        else:
            predict_label.append(0)
    return accuracy_score(paraphrases['Quality'], predict_label)

# print(label_accuracy())
