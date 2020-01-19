from sklearn.model_selection import cross_val_score
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
import numpy as np

fruits = pd.read_table('../resources/fruit_data_with_colors.txt')
X_fruits_2d = fruits[['height', 'width']]
y_fruits_2d = fruits['fruit_label']

X = X_fruits_2d.values
y = y_fruits_2d.values
clf = KNeighborsClassifier(n_neighbors=5)
cv_scores = cross_val_score(clf, X, y, cv=3)

print('Cross validation scores (3-fold):', cv_scores)
print('Mean cross validation scores (3-fold):', np.mean(cv_scores))

