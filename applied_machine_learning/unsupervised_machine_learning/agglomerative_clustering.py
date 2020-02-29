from sklearn.datasets import make_blobs
from sklearn.cluster import AgglomerativeClustering
from applied_machine_learning.fundamentals_of_machine_learning.adspy_shared_utilities import plot_labelled_scatter

X, y = make_blobs(random_state=10)
cls = AgglomerativeClustering(n_clusters=3)
cls_assignment = cls.fit_predict(X)

plot_labelled_scatter(X, cls_assignment, ['Cluster 1', 'Cluster 2', 'Cluster 3'])
