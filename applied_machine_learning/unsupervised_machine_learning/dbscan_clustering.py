from sklearn.datasets import make_blobs
from sklearn.cluster import DBSCAN
from applied_machine_learning.fundamentals_of_machine_learning.adspy_shared_utilities import plot_labelled_scatter

X, y = make_blobs(n_samples=25, random_state=9)

dbscan = DBSCAN(eps=2, min_samples=2)
cls = dbscan.fit_predict(X)

print("Cluster membership values:\n{}".format(cls))

plot_labelled_scatter(X, cls + 1, ['Noise', 'Cluster 0', 'Cluster 1', 'Cluster 2'])