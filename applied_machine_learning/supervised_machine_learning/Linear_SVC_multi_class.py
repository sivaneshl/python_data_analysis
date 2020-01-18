import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from sklearn.model_selection import train_test_split
from sklearn.svm import LinearSVC

fruits = pd.read_table('../resources/fruit_data_with_colors.txt')
target_names_fruits = ['apple', 'mandarin', 'orange', 'lemon']
X_fruits_2d = fruits[['height', 'width']]
y_fruits_2d = fruits['fruit_label']

X_train, X_test, y_train, y_test = train_test_split(X_fruits_2d, y_fruits_2d, random_state=0)

clf = LinearSVC(C=5, random_state=67, max_iter=100000).fit(X_train, y_train)

print('Coefficients:', clf.coef_)
print('Intercepts:', clf.intercept_)

plt.figure(figsize=(6,6))
colors = ['r', 'g', 'b', 'y']
cmap_fruits = ListedColormap(['#FF0000', '#00FF00', '#0000FF','#FFFF00'])
plt.scatter(X_fruits_2d['height'], X_fruits_2d['width'],
           c=y_fruits_2d, cmap=cmap_fruits, edgecolor = 'black', alpha=.7)

x_0_range = np.linspace(-10, 15)

for w, b, color in zip(clf.coef_, clf.intercept_, colors):
    plt.plot(x_0_range, -(x_0_range * w[0] + b) / w[1], c=color, alpha=0.8)

plt.legend(target_names_fruits)
plt.xlabel('height')
plt.ylabel('width')
plt.xlim(-2, 12)
plt.ylim(-2, 15)
plt.show()