import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from applied_machine_learning.fundamentals_of_machine_learning.adspy_shared_utilities import plot_decision_tree
from applied_machine_learning.fundamentals_of_machine_learning.adspy_shared_utilities import plot_feature_importances


iris = load_iris()

X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, random_state=3)

clf = DecisionTreeClassifier().fit(X_train, y_train)
print('Accuracy of Decision tree classifier on training dataset: {:.2f}'.format(clf.score(X_train, y_train)))
print('Accuracy of Decision tree classifier on test dataset: {:.2f}'.format(clf.score(X_test, y_test)))

# Setting max decision tree depth to help avoid overfitting
clf2 = DecisionTreeClassifier(max_depth=3).fit(X_train, y_train)
print('Accuracy of Decision tree classifier (Depth=3) on training dataset: {:.2f}'.format(clf2.score(X_train, y_train)))
print('Accuracy of Decision tree classifier (Depth=3) on test dataset: {:.2f}'.format(clf2.score(X_test, y_test)))

# Visualizing decision trees
plot_decision_tree(clf, iris.feature_names, iris.target_names)
plot_decision_tree(clf2, iris.feature_names, iris.target_names)

# Feature importance
plt.figure(figsize=(10,4), dpi=80)
plot_feature_importances(clf, iris.feature_names)
plt.show()
print('Feature importances: {}'.format(clf.feature_importances_))