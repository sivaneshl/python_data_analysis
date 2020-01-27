import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Lasso
from sklearn.preprocessing import PolynomialFeatures


def part1_scatter():
    plt.figure()
    plt.scatter(X_train, y_train, label='training data')
    plt.scatter(X_test, y_test, label='test data')
    plt.legend(loc=4);
    plt.show()

np.random.seed(0)
n = 15
x = np.linspace(0,10,n) + np.random.randn(n)/5
y = np.sin(x)+x/6 + np.random.randn(n)/10

X_train, X_test, y_train, y_test = train_test_split(x, y, random_state=0)

part1_scatter()

# Question 1
# Write a function that fits a polynomial LinearRegression model on the training data X_train for degrees 1, 3, 6,
# and 9. (Use PolynomialFeatures in sklearn.preprocessing to create the polynomial features and then fit a linear
# regression model) For each model, find 100 predicted values over the interval x = 0 to 10 (e.g. np.linspace(0,10,100))
# and store this in a numpy array. The first row of this array should correspond to the output from the model trained
# on degree 1, the second row degree 3, the third row degree 6, and the fourth row degree 9.

def answer_one():
    result = []
    for deg in [1, 3, 6, 9]:
        poly = PolynomialFeatures(degree=deg)
        X_poly = poly.fit_transform(X_train.reshape(11,-1))
        linreg = LinearRegression().fit(X_poly, y_train)
        X_predict_input = poly.transform(np.linspace(0, 10, 100).reshape(100,-1))
        y_predict_output = linreg.predict(X_predict_input)
        result.append(y_predict_output)
    return result

def plot_one(degree_predictions):
    plt.figure(figsize=(10,5))
    plt.plot(X_train, y_train, 'o', label='training data', markersize=10)
    plt.plot(X_test, y_test, 'o', label='test data', markersize=10)
    for i,degree in enumerate([1,3,6,9]):
        plt.plot(np.linspace(0,10,100), degree_predictions[i], alpha=0.8, lw=2, label='degree={}'.format(degree))
    plt.ylim(-1,2.5)
    plt.legend(loc=4)
    plt.show()

plot_one(answer_one())

# Question 2
# Write a function that fits a polynomial LinearRegression model on the training data X_train for degrees 0 through 9.
# For each model compute the  R2R2  (coefficient of determination) regression score on the training data as well as
# the the test data, and return both of these arrays in a tuple.
# This function should return one tuple of numpy arrays (r2_train, r2_test). Both arrays should have shape (10,)

def answer_two():
    r2_train = np.zeros((10,))
    r2_test = np.zeros((10,))
    for deg in range(0,10):
        poly = PolynomialFeatures(degree=deg)
        X_train_poly = poly.fit_transform(X_train[:, np.newaxis])
        X_test_poly = poly.fit_transform(X_test[:, np.newaxis])
        linreg_train = LinearRegression().fit(X_train_poly, y_train)
        linreg_test = LinearRegression().fit(X_test_poly, y_test)
        r2_train[deg] = linreg_train.score(X_train_poly, y_train)
        r2_test[deg] = linreg_test.score(X_test_poly, y_test)
    return (r2_train, r2_test)


print(answer_two())


# Question 3
# Based on the  R2R2  scores from question 2 (degree levels 0 through 9), what degree level corresponds to a model
# that is underfitting? What degree level corresponds to a model that is overfitting? What choice of degree level
# would provide a model with good generalization performance on this dataset?
#
# Hint: Try plotting the  R2R2  scores from question 2 to visualize the relationship between degree level and  R2R2 .
# Remember to comment out the import matplotlib line before submission.
#
# This function should return one tuple with the degree values in this order: (Underfitting, Overfitting,
# Good_Generalization). There might be multiple correct solutions, however, you only need to return one possible
# solution, for example, (1,2,3).

def answer_three():
    plt.plot(answer_two()[0], label='r2_train')
    plt.plot(answer_two()[1], label='r2_test')
    plt.legend()
    plt.show()
    return (0, 9, 6)

answer_three()


def answer_four():
    poly = PolynomialFeatures(degree=12)
    X_poly_train = poly.fit_transform(X_train[:, np.newaxis])
    X_poly_test = poly.fit_transform(X_test[:, np.newaxis])

    linreg = LinearRegression()
    lassoreg = Lasso(alpha=0.01, max_iter=100000)

    linreg.fit(X_poly_train, y_train)
    lassoreg.fit(X_poly_train, y_train)

    linreg_r2_test_score = linreg.score(X_poly_test, y_test)
    lasso_r2_test_score = lassoreg.score(X_poly_test, y_test)

    return (linreg_r2_test_score, lasso_r2_test_score)

print(answer_four())