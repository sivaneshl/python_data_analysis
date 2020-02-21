# In this assignment you will explore text message data and create models to predict if a message is spam or not.
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.metrics import roc_auc_score

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

spam_data = pd.read_csv('../resources/spam.csv')
spam_data['target'] = np.where(spam_data['target'] == 'spam', 1, 0)
# print(spam_data)

X_train, X_test, y_train, y_test = train_test_split(spam_data['text'],
                                                    spam_data['target'],
                                                    random_state=0)

# Question 1
# What percentage of the documents in spam_data are spam?
# This function should return a float, the percent value (i.e.  ratio∗100).
def answer_one():
    return len(spam_data[spam_data['target']==1]) / len(spam_data) * 100

# Question 2
# Fit the training data X_train using a Count Vectorizer with default parameters.
# What is the longest token in the vocabulary?
# This function should return a string.
def answer_two():
    vect = CountVectorizer().fit(X_train)
    feature_names = np.array(vect.get_feature_names())
    length = [len(token) for token in feature_names]
    return feature_names[np.argmax(length)]

# Question 3
# Fit and transform the training data X_train using a Count Vectorizer with default parameters.
# Next, fit a fit a multinomial Naive Bayes classifier model with smoothing alpha=0.1.
# Find the area under the curve (AUC) score using the transformed test data.
# This function should return the AUC score as a float.
def answer_three():
    vect = CountVectorizer().fit(X_train)
    X_train_vectorized = vect.transform(X_train)

    model = MultinomialNB(alpha=0.1)
    model.fit(X_train_vectorized, y_train)
    predictions = model.predict(vect.transform(X_test))
    return roc_auc_score(y_test, predictions)


# Question 4
# Fit and transform the training data X_train using a Tfidf Vectorizer with default parameters.
# What 20 features have the smallest tf-idf and what 20 have the largest tf-idf?
# Put these features in a two series where each series is sorted by tf-idf value and then alphabetically by
# feature name. The index of the series should be the feature name, and the data should be the tf-idf.
# The series of 20 features with smallest tf-idfs should be sorted smallest tfidf first, the list of 20 features
# with largest tf-idfs should be sorted largest first.
# This function should return a tuple of two series (smallest tf-idfs series, largest tf-idfs series).
def answer_four():
    vect = TfidfVectorizer().fit(X_train)
    X_train_vectorized = vect.transform(X_train)

    tfidf_values = X_train_vectorized.max(0).toarray()[0]
    index = vect.get_feature_names()

    features_series = pd.Series(tfidf_values, index)

    return features_series.nsmallest(20), features_series.nlargest(20)


# Question 5
# Fit and transform the training data X_train using a Tfidf Vectorizer ignoring terms that have a document
# frequency strictly lower than 3.
# Then fit a multinomial Naive Bayes classifier model with smoothing alpha=0.1 and compute the area under
# the curve (AUC) score using the transformed test data.
# This function should return the AUC score as a float.
def answer_five():
    vect = TfidfVectorizer(min_df=3).fit(X_train)
    X_train_vectorized = vect.transform(X_train)
    model = MultinomialNB(alpha=0.1)
    model.fit(X_train_vectorized, y_train)
    predictions = model.predict(vect.transform(X_test))
    return roc_auc_score(y_test, predictions)


# Question 6
# What is the average length of documents (number of characters) for not spam and spam documents?
# This function should return a tuple (average length not spam, average length spam).
def answer_six():
    spam_series = [len(text) for text in (spam_data[spam_data['target']==1]['text'])]
    non_spam_series = [len(text) for text in (spam_data[spam_data['target']==0]['text'])]
    return (np.mean(spam_series), np.mean(non_spam_series))

# The following function has been provided to help you combine new features into the training data:
def add_feature(X, feature_to_add):
    """
    Returns sparse feature matrix with added feature.
    feature_to_add can also be a list of features.
    """
    from scipy.sparse import csr_matrix, hstack
    return hstack([X, csr_matrix(feature_to_add).T], 'csr')


# Question 7
# Fit and transform the training data X_train using a Tfidf Vectorizer ignoring terms that have a document
# frequency strictly lower than 5.
# Using this document-term matrix and an additional feature, the length of document (number of characters),
# fit a Support Vector Classification model with regularization C=10000. Then compute the area under the
# curve (AUC) score using the transformed test data.
# This function should return the AUC score as a float.
def answer_seven():
    vect = TfidfVectorizer(min_df=5).fit(X_train)

    X_train_vectorized = vect.transform(X_train)
    X_test_vectorized = vect.transform(X_test)

    X_train_len = X_train.apply(len)
    X_test_len = X_test.apply(len)

    X_train_added = add_feature(X_train_vectorized, X_train_len)
    X_test_added = add_feature(X_test_vectorized, X_test_len)

    model = SVC(C=10000)
    model.fit(X_train_added, y_train)
    predictions = model.predict(X_test_added)
    return roc_auc_score(y_test, predictions)

# Question 8
# What is the average number of digits per document for not spam and spam documents?
# This function should return a tuple (average # digits not spam, average # digits spam).
def answer_eight():
    spam_digits = spam_data[spam_data['target']==1]['text'].str.count('\d')
    non_spam_digits = spam_data[spam_data['target'] == 0]['text'].str.count('\d')
    return non_spam_digits.mean(), spam_digits.mean()


# Question 9
# Fit and transform the training data X_train using a Tfidf Vectorizer ignoring terms that have a document
# frequency strictly lower than 5 and using word n-grams from n=1 to n=3 (unigrams, bigrams, and trigrams).
# Using this document-term matrix and the following additional features:
# the length of document (number of characters)
# number of digits per document
# fit a Logistic Regression model with regularization C=100. Then compute the area under the curve (AUC)
# score using the transformed test data.
# This function should return the AUC score as a float.
def answer_nine():
    vect = TfidfVectorizer(min_df=5, ngram_range=(1,3)).fit(X_train)

    X_train_vectorized = vect.transform(X_train)
    X_test_vectorized = vect.transform(X_test)

    X_train_len = X_train.apply(len)
    X_test_len = X_test.apply(len)

    X_train_add_len = add_feature(X_train_vectorized, X_train_len)
    X_test_add_len = add_feature(X_test_vectorized, X_test_len)

    X_train_digits_len = X_train.str.count('\d')
    X_test_digits_len = X_test.str.count('\d')

    X_train_final = add_feature(X_train_add_len, X_train_digits_len)
    X_test_final = add_feature(X_test_add_len, X_test_digits_len)

    model = LogisticRegression(C=100, max_iter=10000)
    model.fit(X_train_final, y_train)
    predictions = model.predict(X_test_final)
    return roc_auc_score(y_test, predictions)


# Question 10
# What is the average number of non-word characters (anything other than a letter, digit or underscore)
# per document for not spam and spam documents?
# Hint: Use \w and \W character classes
# This function should return a tuple (average # non-word characters not spam, average # non-word characters spam).
def answer_ten():
    spam_nonword = spam_data[spam_data['target'] == 1]['text'].str.count('\W')
    non_spam_nonword = spam_data[spam_data['target'] == 0]['text'].str.count('\W')
    return non_spam_nonword.mean(), spam_nonword.mean()


# Question 11
# Fit and transform the training data X_train using a Count Vectorizer ignoring terms that have a
# document frequency strictly lower than 5 and using character n-grams from n=2 to n=5.
# To tell Count Vectorizer to use character n-grams pass in analyzer='char_wb' which creates character
# n-grams only from text inside word boundaries. This should make the model more robust to spelling mistakes.
# Using this document-term matrix and the following additional features:
# the length of document (number of characters)
# number of digits per document
# number of non-word characters (anything other than a letter, digit or underscore.)
# fit a Logistic Regression model with regularization C=100. Then compute the area under the curve (AUC)
# score using the transformed test data.
# Also find the 10 smallest and 10 largest coefficients from the model and return them along with the AUC
# score in a tuple.
# The list of 10 smallest coefficients should be sorted smallest first, the list of 10 largest coefficients
# should be sorted largest first.
# The three features that were added to the document term matrix should have the following names should they
# appear in the list of coefficients: ['length_of_doc', 'digit_count', 'non_word_char_count']
# This function should return a tuple (AUC score as a float, smallest coefs list, largest coefs list).
def answer_eleven():
    import re

    vect =  TfidfVectorizer(min_df=5, analyzer='char_wb', ngram_range=(2,5)).fit(X_train)

    X_train_vectorized = vect.transform(X_train)
    X_test_vectorized = vect.transform(X_test)

    X_train_len = X_train.apply(len)
    X_test_len = X_test.apply(len)

    # X_train_digits_len = X_train.str.count('\d')
    # X_test_digits_len = X_test.str.count('\d')
    f = lambda x: sum([c.isdigit() for c in x])
    X_train_digits_len = X_train.apply(f)
    X_test_digits_len = X_test.apply(f)

    # X_train_spam_char_len = X_train.str.count('\W')
    # X_test_spam_char_len = X_test.str.count('\W')
    X_train_spam_char_len = X_train.apply(lambda x: len(re.findall('\W', x)))
    X_test_spam_char_len = X_test.apply(lambda x: len(re.findall('\W', x)))

    X_train_add_3 = add_feature(add_feature(add_feature(X_train_vectorized, X_train_len),
                                            X_train_digits_len),
                                X_train_spam_char_len)
    X_test_add_3 = add_feature(add_feature(add_feature(X_test_vectorized, X_test_len),
                                            X_test_digits_len),
                                X_test_spam_char_len)
    # X_train_add_2 = add_feature(X_train_add_1, X_train_digits_len)
    # X_train_add_3 = add_feature(X_train_add_2, X_train_spam_char_len)

    # X_test_add_1 = add_feature(X_test_vectorized, X_test_len)
    # X_test_add_2 = add_feature(X_test_add_1, X_test_digits_len)
    # X_test_add_3 = add_feature(X_test_add_2, X_test_spam_char_len)

    model = LogisticRegression(C=100, max_iter=10000)
    model.fit(X_train_add_3, y_train)
    predictions = model.predict(X_test_add_3)

    feature_names = np.array(vect.get_feature_names() + ['length_of_doc', 'digit_count', 'non_word_char_count'])

    sorted_coef_index = model.coef_[0].argsort()
    smallest_coef_list = list(feature_names[sorted_coef_index[:10]])
    largest_coef_list = list(feature_names[sorted_coef_index[:-11:-1]])

    return (roc_auc_score(y_test, predictions), smallest_coef_list, largest_coef_list)



def answer_twelve():
    import re
    f = lambda x: sum([c.isdigit() for c in x])
    vect = CountVectorizer(min_df=5, ngram_range=(2, 5), analyzer='char_wb').fit(X_train)

    vect = TfidfVectorizer(min_df=5, analyzer='char_wb', ngram_range=(2, 5)).fit(X_train)

    X_train_vectorized = vect.transform(X_train)
    X_test_vectorized = vect.transform(X_test)

    X_train_len = X_train.apply(len)
    X_test_len = X_test.apply(len)

    X_train_digits_len = X_train.str.count('\d')
    X_test_digits_len = X_test.str.count('\d')

    X_train_spam_char_len = X_train.str.count('\W')
    X_test_spam_char_len = X_test.str.count('\W')

    X_train_add_3 = add_feature(add_feature(add_feature(X_train_vectorized, X_train_len),
                                            X_train_digits_len),
                                X_train_spam_char_len)
    X_test_add_3 = add_feature(add_feature(add_feature(X_test_vectorized, X_test_len),
                                            X_test_digits_len),
                                X_test_spam_char_len)

    model = LogisticRegression(C=100, max_iter=10000).fit(X_train_add_3, y_train)
    predictions = model.predict(X_test_add_3)
    AUC_score = roc_auc_score(y_test, predictions)
    feature_names = np.array(vect.get_feature_names() + ['length_of_doc', 'digit_count', 'non_word_char_count'])
    sorted_coef_index = model.coef_[0].argsort()
    smallest_list = feature_names[sorted_coef_index[:10]]
    largest_list = feature_names[sorted_coef_index[:-11:-1]]
    return (AUC_score, list(smallest_list), list(largest_list))

print(answer_twelve())