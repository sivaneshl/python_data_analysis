# Ridge regression with regularization parameter: alpha

import numpy as np
from applied_machine_learning.fundamentals_of_machine_learning.adspy_shared_utilities import load_crime_dataset
from sklearn.preprocessing import MinMaxScaler
from sklearn.linear_model import Ridge
from sklearn.model_selection import train_test_split

scalar = MinMaxScaler()
(X_crime, y_crime) = load_crime_dataset()

X_train, X_test, y_train, y_test = train_test_split(X_crime, y_crime, random_state=0)
X_train_scaled = scalar.fit_transform(X_train)
X_test_scaled = scalar.fit_transform(X_test)

print('Crime Dataset')
print('Ridge regression - Effect of alpha regularization parameter')
for this_alpha in [0, 1, 10, 20, 50, 100, 1000]:
    linridge = Ridge(alpha=this_alpha).fit(X_train_scaled, y_train)
    print('Alpha = {}'.format(this_alpha))
    print('R-squared score (training): {:.3f}'.format(linridge.score(X_train_scaled, y_train)))
    print('R-squared score (test): {:.3f}'.format(linridge.score(X_test_scaled, y_test)))
    print('Number of non-zero features: {}'.format(np.sum(linridge.coef_ != 0)))

