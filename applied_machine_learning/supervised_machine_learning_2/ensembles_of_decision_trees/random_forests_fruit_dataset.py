import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from applied_machine_learning.fundamentals_of_machine_learning.adspy_shared_utilities import plot_class_regions_for_classifier_subplot

fruits = pd.read_table('../../resources/fruit_data_with_colors.txt')

feature_names_fruits = ['height', 'width', 'mass', 'color_score']
target_fruit_names = ['apple', 'mandarin', 'orange', 'lemon']
title = 'Random Forest, fruits dataset, default settings'
pair_list = [[0,1], [0,2], [0,3], [1,2], [1,3], [2,3]]

X_fruits = fruits[feature_names_fruits]
y_fruits = fruits['fruit_label']

X_train, X_test, y_train, y_test = train_test_split(X_fruits.values,
                                                    y_fruits.values,
                                                    random_state=0)

fig, subaxes = plt.subplots(6, 1, figsize=(6,50))
for pair, axes in zip(pair_list, subaxes):
    X = X_train[:, pair]
    y = y_train

    clf = RandomForestClassifier(n_jobs=-1).fit(X, y)
    plot_class_regions_for_classifier_subplot(clf, X, y, None, None, title, axes, target_fruit_names)

    axes.set_xlabel(feature_names_fruits[pair[0]])
    axes.set_ylabel(feature_names_fruits[pair[1]])

plt.tight_layout()
plt.show()

clf = RandomForestClassifier(n_jobs=-1).fit(X_train, y_train)
print('Random Forest, Fruit dataset, default settings')
print('Accuracy of RF classifier on training set: {:.2f}'
     .format(clf.score(X_train, y_train)))
print('Accuracy of RF classifier on test set: {:.2f}'
     .format(clf.score(X_test, y_test)))

