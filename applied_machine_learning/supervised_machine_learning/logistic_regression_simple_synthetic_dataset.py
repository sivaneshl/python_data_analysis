# Logistic regression on simple synthetic dataset

import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import make_classification
from applied_machine_learning.fundamentals_of_machine_learning.adspy_shared_utilities import plot_class_regions_for_classifier_subplot

X_C2, y_C2 = make_classification(n_samples=100, n_features=2, n_redundant=0, n_informative=2,
                                 n_clusters_per_class=1, flip_y=0.1, class_sep=0.5, random_state=0)

X_train, X_test, y_train, y_test = train_test_split(X_C2, y_C2, random_state=0)

clf = LogisticRegression().fit(X_train, y_train)

fig, subaxes = plt.subplots(1, 1, figsize=(7, 5))
title = 'Logistic regression, simple synthetic dataset C = {:.3f}'.format(1.0)
plot_class_regions_for_classifier_subplot(clf, X_train, y_train, None, None, title, subaxes)
plt.show()

print('Accuracy of Logistic regression classifier on training dataset: {:.3f}'.format(clf.score(X_train, y_train)))
print('Accuracy of Logistic regression classifier on test dataset: {:.3f}'.format(clf.score(X_test, y_test)))

