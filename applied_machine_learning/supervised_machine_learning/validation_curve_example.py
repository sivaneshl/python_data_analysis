import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.svm import SVC
from sklearn.model_selection import validation_curve

fruits = pd.read_table('../resources/fruit_data_with_colors.txt')
X_fruits_2d = fruits[['height', 'width']]
y_fruits_2d = fruits['fruit_label']

X = X_fruits_2d.values
y = y_fruits_2d.values

param_range = np.linspace(-3, 3, 4)
train_scores, test_scores = validation_curve(SVC(), X, y,
                                             param_name='gamma', param_range=param_range,
                                             cv=3)

print(train_scores)
print(test_scores)


plt.figure()

train_scores_mean = np.mean(train_scores, axis=1)
train_scores_std = np.std(train_scores, axis=1)
test_scores_mean = np.mean(test_scores, axis=1)
test_scores_std = np.std(test_scores, axis=1)

plt.title('Validation Curve with SVM')
plt.xlabel('$\gamma$ (gamma)')
plt.ylabel('Score')
plt.ylim(0.0, 1.1)
lw = 2

plt.semilogx(param_range, train_scores_mean, label='Training score', color='darkorange', lw=lw)

plt.fill_between(param_range, train_scores_mean - train_scores_std, train_scores_mean + train_scores_std,
                 alpha=0.2, color='darkorange', lw=lw)

plt.semilogx(param_range, test_scores_mean, label='Cross-validation score', color='navy', lw=lw)

plt.fill_between(param_range, test_scores_mean - test_scores_std, test_scores_mean + test_scores_std,
                 alpha=0.2, color='navy', lw=lw)

plt.legend(loc='best')
plt.show()

