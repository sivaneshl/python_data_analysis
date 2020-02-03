import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import ward, dendrogram
from sklearn.datasets import make_blobs
from applied_machine_learning.fundamentals_of_machine_learning.adspy_shared_utilities import plot_labelled_scatter

X, y = make_blobs(random_state=10, n_samples=10)
plot_labelled_scatter(X, y, ['Cluster 1', 'Cluster 2', 'Cluster 3'])
print(X)

plt.figure()
dendrogram(ward(X))
plt.show()



