from sklearn.cluster import KMeans
from sklearn.preprocessing import MinMaxScaler
import pandas as pd
import matplotlib.pyplot as plt
from applied_machine_learning.fundamentals_of_machine_learning.adspy_shared_utilities import plot_labelled_scatter

fruits = pd.read_table('../resources/fruit_data_with_colors.txt')
feature_names_fruits = ['height', 'width', 'mass', 'color_score']
target_fruit_names = ['apple', 'mandarin', 'orange', 'lemon']
X_fruits = fruits[feature_names_fruits].values
y_fruits = fruits[['fruit_label']] - 1
X_fruits_normalized = MinMaxScaler().fit(X_fruits).transform(X_fruits)

kmeans = KMeans(n_clusters=4, random_state=0)
kmeans.fit(X_fruits_normalized)

plot_labelled_scatter(X_fruits_normalized, kmeans.labels_,
                      ['Cluster 1', 'Cluster 2', 'Cluster 3', 'Cluster 4'])

