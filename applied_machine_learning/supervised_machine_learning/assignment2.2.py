import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.model_selection import validation_curve

mush_df = pd.read_csv('C:/python_data_analysis/applied_machine_learning/resources/mushroom.csv')
mush_df2 = pd.get_dummies(mush_df)

X_mush = mush_df2.iloc[:,2:]
y_mush = mush_df2.iloc[:,1]

# use the variables X_train2, y_train2 for Question 5
X_train2, X_test2, y_train2, y_test2 = train_test_split(X_mush, y_mush, random_state=0)

# For performance reasons in Questions 6 and 7, we will create a smaller version of the
# entire mushroom dataset for use in those questions.  For simplicity we'll just re-use
# the 25% test split created above as the representative subset.
#
# Use the variables X_subset, y_subset for Questions 6 and 7.
X_subset = X_test2
y_subset = y_test2

# Question 5
# Using X_train2 and y_train2 from the preceeding cell, train a DecisionTreeClassifier with default parameters and
# random_state=0. What are the 5 most important features found by the decision tree?
#
# As a reminder, the feature names are available in the X_train2.columns property, and the order of the features in
# X_train2.columns matches the order of the feature importance values in the classifier's feature_importances_
# property.
#
# This function should return a list of length 5 containing the feature names in descending order of importance.
#
# Note: remember that you also need to set random_state in the DecisionTreeClassifier.

def answer_five():
    clf = DecisionTreeClassifier(random_state=0)
    clf.fit(X_train2, y_train2)
    dict = {key:value for key, value in zip(X_train2.columns, clf.feature_importances_)}
    result = [key for key,_ in sorted(dict.items(), key=lambda item: item[1], reverse=True)[:5]]
    return result

print(answer_five())

# Question 6
# For this question, we're going to use the validation_curve function in sklearn.model_selection to determine training and test scores for a Support Vector Classifier (SVC) with varying parameter values. Recall that the validation_curve function, in addition to taking an initialized unfitted classifier object, takes a dataset as input and does its own internal train-test splits to compute results.
#
# Because creating a validation curve requires fitting multiple models, for performance reasons this question will use just a subset of the original mushroom dataset: please use the variables X_subset and y_subset as input to the validation curve function (instead of X_mush and y_mush) to reduce computation time.
#
# The initialized unfitted classifier object we'll be using is a Support Vector Classifier with radial basis kernel. So your first step is to create an SVC object with default parameters (i.e. kernel='rbf', C=1) and random_state=0. Recall that the kernel width of the RBF kernel is controlled using the gamma parameter.
#
# With this classifier, and the dataset in X_subset, y_subset, explore the effect of gamma on classifier accuracy by using the validation_curve function to find the training and test scores for 6 values of gamma from 0.0001 to 10 (i.e. np.logspace(-4,1,6)). Recall that you can specify what scoring metric you want validation_curve to use by setting the "scoring" parameter. In this case, we want to use "accuracy" as the scoring metric.
#
# For each level of gamma, validation_curve will fit 3 models on different subsets of the data, returning two 6x3 (6 levels of gamma x 3 fits per level) arrays of the scores for the training and test sets.
#
# Find the mean score across the three models for each level of gamma for both arrays, creating two arrays of length 6, and return a tuple with the two arrays.
#
# e.g.
#
# if one of your array of scores is
#
# array([[ 0.5,  0.4,  0.6],
#        [ 0.7,  0.8,  0.7],
#        [ 0.9,  0.8,  0.8],
#        [ 0.8,  0.7,  0.8],
#        [ 0.7,  0.6,  0.6],
#        [ 0.4,  0.6,  0.5]])
# it should then become
#
# array([ 0.5,  0.73333333,  0.83333333,  0.76666667,  0.63333333, 0.5])
# This function should return one tuple of numpy arrays (training_scores, test_scores) where each array in the tuple has shape (6,).

def answer_six():
    clf = SVC(random_state=0)
    val_score = validation_curve(clf, X_subset, y_subset, 'gamma', np.logspace(-4,1,6), n_jobs=-1, scoring='accuracy')
    training_scores = val_score[0].mean(axis=1)
    test_scores = val_score[1].mean(axis=1)
    return (training_scores, test_scores)

# print(answer_six())


# Question 7
# Based on the scores from question 6, what gamma value corresponds to a model that is underfitting (and has the worst test set accuracy)? What gamma value corresponds to a model that is overfitting (and has the worst test set accuracy)? What choice of gamma would be the best choice for a model with good generalization performance on this dataset (high accuracy on both training and test set)?
#
# Hint: Try plotting the scores from question 6 to visualize the relationship between gamma and accuracy. Remember to comment out the import matplotlib line before submission.
#
# This function should return one tuple with the degree values in this order: (Underfitting, Overfitting, Good_Generalization) Please note there is only one correct solution.

def answer_seven():

    # plt.plot(answer_six()[0], label='training accuracy')
    # plt.plot(answer_six()[1], label='test accuracy')
    # plt.legend()
    # plt.show()

    deg = np.logspace(-4,1,6)
    print (deg[0], deg[5], deg[3])
    print (np.logspace(-4, 1, 6)[0], np.logspace(-4, 1, 6)[5], np.logspace(-4, 1, 6)[3])

answer_seven()