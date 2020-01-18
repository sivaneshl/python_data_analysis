import matplotlib.pyplot as plt
from sklearn.svm import LinearSVC
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from applied_machine_learning.fundamentals_of_machine_learning.adspy_shared_utilities import plot_class_regions_for_classifier_subplot


X_C2, y_C2 = make_classification(n_samples=100, n_features=2, n_redundant=0, n_informative=2,
                                 n_clusters_per_class=1, flip_y=0.1, class_sep=0.5, random_state=0)
X_train, x_test, y_train, y_test = train_test_split(X_C2, y_C2, random_state=0)

fig, subaxes = plt.subplots(1,3,figsize=(9,3))
for this_C, subplot in zip([0.00001, 1, 100], subaxes):
    clf = LinearSVC(C=this_C).fit(X_train, y_train)
    title = 'Linear SVC, C = {:.5f}'.format(this_C)
    plot_class_regions_for_classifier_subplot(clf, X_train, y_train, None, None, title, subplot)
plt.show()
