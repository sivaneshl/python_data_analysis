# Lasso regression

import numpy as np
from sklearn.linear_model import Lasso
from applied_machine_learning.fundamentals_of_machine_learning.adspy_shared_utilities import load_crime_dataset
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split

scalar = MinMaxScaler()
(X_crime, y_crime) = load_crime_dataset()

X_train, X_test, y_train, y_test = train_test_split(X_crime, y_crime, random_state=0)
X_train_scaled = scalar.fit_transform(X_train)
X_test_scaled = scalar.fit_transform(X_test)

linlasso = Lasso(alpha=2.0, max_iter=10000).fit(X_train_scaled, y_train)

print('Crime dataset')
print('lasso regression linear model intercept: {}'.format(linlasso.intercept_))
print('lasso regression linear model coeff: {}'.format(linlasso.coef_))
print('Non-zero features: {}'.format(np.sum(linlasso.coef_ != 0)))
print('R-squared score training: {:.3f}'.format(linlasso.score(X_train_scaled, y_train)))
print('R-squared score test: {:.3f}'.format(linlasso.score(X_test_scaled, y_test)))
print('Features with non-zero weight (sorted by absolute magnitude): ')
for e in sorted (list(zip(list(X_crime), linlasso.coef_)), key=lambda e: -abs(e[1])):
    if e[1] != 0:
        print('\t{}, {:.3f}'.format(e[0], e[1]))


# Lasso regression with regularization parameter: alpha

print('Lasso regression: Effect of alpha regularization\n parameter on number of features kept in final model\n')
for alpha in [0.5, 1, 2, 3, 5, 10, 15, 20, 30, 50]:
    linlasso = Lasso(alpha=alpha, max_iter=10000).fit(X_train_scaled, y_train)
    print('Alpha = {}'.format(alpha))
    print('Features kept: {}'.format(np.sum(linlasso.coef_ != 0)))
    print('R-squared score training: {:.3f}'.format(linlasso.score(X_train_scaled, y_train)))
    print('R-squared score test: {:.3f}'.format(linlasso.score(X_test_scaled, y_test)))

