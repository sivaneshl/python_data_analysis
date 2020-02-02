from applied_machine_learning.fundamentals_of_machine_learning.adspy_shared_utilities import plot_class_regions_for_classifier
from sklearn.neural_network import MLPClassifier
from sklearn.datasets import make_blobs
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

X_D2, y_D2 = make_blobs(n_samples=100, n_features=2, centers=8, cluster_std=1.3, random_state=4)
y_D2 = y_D2 % 2
X_train, X_test, y_train, y_test = train_test_split(X_D2, y_D2, random_state=0)

nnclf = MLPClassifier(hidden_layer_sizes=[10, 10], solver='lbfgs', random_state=0).fit(X_train, y_train)
title = 'Dataset 1: Neural net classifier, 2 layers, 10/10 units'
plot_class_regions_for_classifier(nnclf, X_train, y_train, X_test, y_test, title)
plt.show()