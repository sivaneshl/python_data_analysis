import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

# read the data
df = pd.read_csv('../resources/Amazon_Unlocked_Mobile.csv')

# clean-up data
df.dropna(inplace=True)
df = df[df['Rating'] != 3]
df['PositivelyRated'] = np.where(df['Rating'] > 3, 1, 0)

# slicing a subset of every 10th row
df = df[::100]

# Most ratings are positive
print(df['PositivelyRated'].mean())

# Split data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(df['Reviews'], df['PositivelyRated'], random_state=0)

print('X_train first entry:\n\n', X_train.iloc[0])
print('\n\nX_train shape: ', X_train.shape)

# CountVectorizer
# Fit the CountVectorizer to the training data
vect = CountVectorizer().fit(X_train)
print(vect.get_feature_names())
print(len(vect.get_feature_names()))

# transform the documents in the training data to a document-term matrix
X_train_vectorized = vect.transform(X_train)
print(X_train_vectorized)

# Train the model
model = LogisticRegression()
model.fit(X_train_vectorized, y_train)
# Predict the transformed test documents
predictions = model.predict(vect.transform(X_test))
print('AUC : ', roc_auc_score(y_test, predictions))

# get the feature names as numpy array
feature_names = np.array(vect.get_feature_names())
# Sort the coefficients from the model
sorted_coef_index = model.coef_[0].argsort()
# Find the 10 smallest and 10 largest coefficients
# The 10 largest coefficients are being indexed using [:-11:-1]
# so the list returned is in order of largest to smallest
print('Smallest Coeffs : \n{}\n'.format(feature_names[sorted_coef_index[:10]]))
print('Largest Coeffs :  \n{}\n'.format(feature_names[sorted_coef_index[:-11:-1]]))


# Tfidf
# Fit the TfidfVectorizer to the training data specifiying a minimum document frequency of 5
vect = TfidfVectorizer(min_df=5).fit(X_train)
print(len(vect.get_feature_names()))

X_train_vectorized = vect.transform(X_train)
model = LogisticRegression()
model.fit(X_train_vectorized, y_train)
predictions = model.predict(vect.transform(X_test))
print('AUC : ',  roc_auc_score(y_test, predictions))

feature_names = np.array(vect.get_feature_names())
sorted_tfidf_index = X_train_vectorized.max(0).toarray()[0].argsort()
# print(feature_names)
# print(sorted_tfidf_index)
print('Smallest tfidf : \n{}\n'.format(feature_names[sorted_tfidf_index[:10]]))
print('Largest tfidf :  \n{}\n'.format(feature_names[sorted_tfidf_index[:-11:-1]]))

sorted_coef_index = model.coef_[0].argsort()
print('Smallest Coeffs : \n{}\n'.format(feature_names[sorted_coef_index[:10]]))
print('Largest Coeffs :  \n{}\n'.format(feature_names[sorted_coef_index[:-11:-1]]))

# These reviews are treated the same by our current model
print(model.predict(vect.transform(['not an issue, phone is working',
                                    'an issue, phone is not working'])))

# n-grams
# Fit the CountVectorizer to the training data specifiying a minimum
# document frequency of 5 and extracting 1-grams and 2-grams
vect = CountVectorizer(ngram_range=(1, 3), min_df=5).fit(X_train)
X_train_vectorized = vect.transform(X_train)
print(len(vect.get_feature_names()))

model = LogisticRegression()
model.fit(X_train_vectorized, y_train)
predictions = model.predict(vect.transform(X_test))
print('AUC : ', roc_auc_score(y_test, predictions))

feature_names = np.array(vect.get_feature_names())
sorted_coef_index = model.coef_[0].argsort()
print('Smallest Coefs : \n{}\n'.format(feature_names[sorted_coef_index[:10]]))
print('Largest Coefs : \n{}\n'.format(feature_names[sorted_coef_index[:-11:-1]]))

# These reviews are now correctly identified
print(model.predict(vect.transform(['no issue, phone is working',
                                    'an issue, phone is not working'])))
