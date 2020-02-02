from sklearn.manifold import TSNE
from sklearn.preprocessing import StandardScaler
import pandas as pd
import matplotlib.pyplot as plt

from applied_machine_learning.fundamentals_of_machine_learning.adspy_shared_utilities import plot_labelled_scatter

tsne = TSNE(random_state = 0)

fruits = pd.read_table('../resources/fruit_data_with_colors.txt')
feature_names_fruits = ['height', 'width', 'mass', 'color_score']
target_fruit_names = ['apple', 'mandarin', 'orange', 'lemon']
X_fruits = fruits[feature_names_fruits]
y_fruits = fruits['fruit_label']


# each feature should be centered (zero mean) and with unit variance
X_fruits_normalized = StandardScaler().fit(X_fruits).transform(X_fruits)

X_tsne = tsne.fit_transform(X_fruits_normalized)

plot_labelled_scatter(X_tsne, y_fruits,
    ['apple', 'mandarin', 'orange', 'lemon'])
plt.xlabel('First t-SNE feature')
plt.ylabel('Second t-SNE feature')
plt.title('Fruits dataset t-SNE')