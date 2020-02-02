from applied_machine_learning.fundamentals_of_machine_learning.adspy_shared_utilities import plot_labelled_scatter
from sklearn.preprocessing import StandardScaler
from sklearn.manifold import MDS
import pandas as pd
import matplotlib.pyplot as plt

fruits = pd.read_table('../resources/fruit_data_with_colors.txt')
feature_names_fruits = ['height', 'width', 'mass', 'color_score']
target_fruit_names = ['apple', 'mandarin', 'orange', 'lemon']
X_fruits = fruits[feature_names_fruits]
y_fruits = fruits['fruit_label']


# each feature should be centered (zero mean) and with unit variance
X_fruits_normalized = StandardScaler().fit(X_fruits).transform(X_fruits)

mds = MDS(n_components = 2)

X_fruits_mds = mds.fit_transform(X_fruits_normalized)

plot_labelled_scatter(X_fruits_mds, y_fruits, ['apple', 'mandarin', 'orange', 'lemon'])
plt.xlabel('First MDS feature')
plt.ylabel('Second MDS feature')
plt.title('Fruit sample dataset MDS')
