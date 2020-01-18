# Logistic Regression

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from applied_machine_learning.fundamentals_of_machine_learning.adspy_shared_utilities import plot_class_regions_for_classifier_subplot

fruits = pd.read_table('../resources/fruit_data_with_colors.txt')
X_fruits_2d = fruits[['height', 'width']]
y_fruits_2d = fruits['fruit_label']
y_fruits_apple = y_fruits_2d == 1

X_train, X_test, y_train, y_test = train_test_split(X_fruits_2d.values,
                                                    y_fruits_apple.values,
                                                    random_state=0)
clf = LogisticRegression(C=100).fit(X_train, y_train)

fig, subaxes = plt.subplots(1, 1, figsize=(7, 5))
plot_class_regions_for_classifier_subplot(clf, X_train, y_train, None, None,
                                          'Logistic regression for binary classification\nFruit dataset: Apple vs others',
                                          subaxes)
subaxes.set_xlabel('height')
subaxes.set_ylabel('width')

h = 6
w = 8
print('A fruit with height {} and width {} is predicted as {}'
      .format(h, w, ['not an apple', 'an apple'][clf.predict([[h, w]])[0]]))

h = 10
w = 7
print('A fruit with height {} and width {} is predicted as {}'
      .format(h, w, ['not an apple', 'an apple'][clf.predict([[h, w]])[0]]))


plt.show()
print('Accuracy of logistic regression on training dataset: {:.3f}'.format(clf.score(X_train, y_train)))
print('Accuracy of logistic regression on test dataset: {:.3f}'.format(clf.score(X_test, y_test)))


