import matplotlib.pyplot as plt
from sklearn.svm import SVC
from sklearn.datasets import make_blobs
from sklearn.model_selection import train_test_split
from applied_machine_learning.fundamentals_of_machine_learning.adspy_shared_utilities import plot_class_regions_for_classifier


X_D2, y_D2 = make_blobs(n_samples=100, n_features=2, centers=8, cluster_std=1.3, random_state=4)
y_D2 = y_D2 % 2
X_train, X_test, y_train, y_test = train_test_split(X_D2, y_D2, random_state=0)

# The default SVC kernel is radial basis function (RBF)
plot_class_regions_for_classifier(SVC(kernel='rbf', gamma='auto').fit(X_train, y_train),
                                  X_train, y_train, None, None,
                                  'Support Vector Classifier: RBF kernel')

# Compare decision boundries with polynomial kernel, degree = 3
plot_class_regions_for_classifier(SVC(kernel='poly', degree=3, gamma='auto').fit(X_train, y_train),
                                  X_train, y_train, None, None,
                                  'Support Vector Classifier: Polynomial kernel, degree = 3')

plt.show()