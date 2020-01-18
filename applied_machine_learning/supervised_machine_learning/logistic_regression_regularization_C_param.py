# Logistic regression regularization: C parameter

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

fig, subaxes = plt.subplots(3,1,figsize=(4,10))

for this_C, subplot in zip([0.1, 1, 100], subaxes):
    clf = LogisticRegression(C=this_C).fit(X_train, y_train)
    title = 'Logistic regression, simple synthetic dataset C = {:.3f}'.format(this_C)
    plot_class_regions_for_classifier_subplot(clf, X_train, y_train, None, None, title, subplot)
    print('C={:.3f}'.format(this_C))
    print('Training dataset accuracy: {:.3f}'.format(clf.score(X_train, y_train)))
    print('Testing dataset accuracy: {:.3f}'.format(clf.score(X_test, y_test)))

plt.tight_layout()
plt.show()