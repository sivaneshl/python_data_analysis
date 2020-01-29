# Assignment 3 - Evaluation
#
# In this assignment you will train several models and evaluate how effectively
# they predict instances of fraud using data based on this dataset from Kaggle.
# Each row in fraud_data.csv corresponds to a credit card transaction. Features
# include confidential variables V1 through V28 as well as Amount which is the
# amount of the transaction.
# The target is stored in the class column, where a value of 1 corresponds to an
# instance of fraud and 0 corresponds to an instance of not fraud.

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.dummy import DummyClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, precision_score, recall_score, precision_score
from sklearn.metrics import confusion_matrix, precision_recall_curve, roc_curve
from sklearn.linear_model import LogisticRegression

# Question 1
# Import the data from fraud_data.csv. What percentage of the observations in the
# dataset are instances of fraud?
# This function should return a float between 0 and 1.

df = pd.read_csv('/home/sivaneshl/python_data_analysis/applied_machine_learning/resources/fraud_data.csv')

def answer_one():
    fraud = df[df['Class']==1]
    return len(fraud)/len(df)

# Use X_train, X_test, y_train, y_test for all of the following questions
X = df.iloc[:,:-1]
y = df.iloc[:,-1]

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

# Question 2
# Using X_train, X_test, y_train, and y_test (as defined above), train a dummy
# classifier that classifies everything as the majority class of the training data.
# What is the accuracy of this classifier? What is the recall?
# This function should a return a tuple with two floats, i.e. (accuracy score, recall score).
def answer_two():
    dummy_majority = DummyClassifier(strategy='most_frequent').fit(X_train, y_train)
    y_majority_predicted = dummy_majority.predict(X_test)
    acc = dummy_majority.score(X_train, y_train)
    dummy_accuracy = accuracy_score(y_test, y_majority_predicted)
    dummy_recall = recall_score(y_test, y_majority_predicted)
    return (dummy_accuracy, dummy_recall)

# Question 3
# Using X_train, X_test, y_train, y_test (as defined above), train a SVC classifer
# using the default parameters. What is the accuracy, recall, and precision of this classifier?
# This function should a return a tuple with three floats, i.e. (accuracy score, recall score, precision score).
def answer_three():
    svm = SVC(gamma='auto').fit(X_train, y_train)
    y_svm_predicted = svm.predict(X_test)
    svm_accuracy = accuracy_score(y_test, y_svm_predicted)
    acc = svm.score(X_train, y_train)
    svm_recall = recall_score(y_test, y_svm_predicted)
    svm_precision = precision_score(y_test, y_svm_predicted)
    return (svm_accuracy, svm_recall, svm_precision)

# Question 4
# Using the SVC classifier with parameters {'C': 1e9, 'gamma': 1e-07}, what is the
# confusion matrix when using a threshold of -220 on the decision function. Use X_test and y_test.
# This function should return a confusion matrix, a 2x2 numpy array with 4 integers.
def answer_four():
    svm = SVC(C=1e9, gamma=1e-07).fit(X_train, y_train)
    y_decision = svm.decision_function(X_test) > -220
    confusion = confusion_matrix(y_test, y_decision)
    return confusion

# Question 5
# Train a logisitic regression classifier with default parameters using X_train and y_train.
# For the logisitic regression classifier, create a precision recall curve and a roc curve
# using y_test and the probability estimates for X_test (probability it is fraud).
# Looking at the precision recall curve, what is the recall when the precision is 0.75?
# Looking at the roc curve, what is the true positive rate when the false positive rate is 0.16?
# This function should return a tuple with two floats, i.e. (recall, true positive rate).
def answer_five():
    logreg = LogisticRegression(max_iter=10000).fit(X_train, y_train)
    y_proba_logreg = logreg.fit(X_train, y_train).predict_proba(X_test)[:,1]
    precision, recall, threshold = precision_recall_curve(y_test, y_proba_logreg)
    fpr_logreg, tpr_logreg, _ = roc_curve(y_test, y_proba_logreg)

    plt.figure()
    plt.xlim([0.0, 1.01])
    plt.ylim([0.0, 1.01])
    plt.plot(precision, recall, label='Precision-Recall Curve')
    plt.xlabel('Precision', fontsize=16)
    plt.ylabel('Recall', fontsize=16)
    plt.show()

    plt.figure()
    plt.xlim([-0.01, 1.00])
    plt.ylim([-0.01, 1.01])
    plt.plot(fpr_logreg, tpr_logreg, lw=3, label='LogRegr ROC curve')
    plt.xlabel('False Positive Rate', fontsize=16)
    plt.ylabel('True Positive Rate', fontsize=16)
    plt.show()

# Question 6
# Perform a grid search over the parameters listed below for a Logisitic Regression classifier,
# using recall for scoring and the default 3-fold cross validation.
# 'penalty': ['l1', 'l2']
# 'C':[0.01, 0.1, 1, 10, 100]
# From .cv_results_, create an array of the mean test scores of each parameter combination.
# This function should return a 5 by 2 numpy array with 10 floats.
# Note: do not return a DataFrame, just the values denoted by '?' above in a numpy array.
# You might need to reshape your raw result to meet the format we are looking for.
# Use the following function to help visualize results from the grid search
def GridSearch_Heatmap(scores):
    plt.figure()
    sns.heatmap(scores.reshape(5,2), xticklabels=['l1','l2'], yticklabels=[0.01, 0.1, 1, 10, 100])
    plt.yticks(rotation=0);
    plt.show()

def answer_six():
    grid_values = {'penalty': ['l1', 'l2'], 'C': [0.01, 0.1, 1, 10, 100]}
    clf = GridSearchCV(LogisticRegression(max_iter=10000), param_grid=grid_values, scoring='recall')
    clf.fit(X_train, y_train)
    scores = clf.cv_results_['mean_test_score'].reshape(5,2)
    print(scores)
    GridSearch_Heatmap(scores)


print(answer_one())
# print(answer_two())
# print(answer_three())
# print(answer_four())
# answer_five()
answer_six()
