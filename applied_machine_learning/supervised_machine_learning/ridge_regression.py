from applied_machine_learning.fundamentals_of_machine_learning.adspy_shared_utilities import load_crime_dataset
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Ridge
import numpy as np

# Communities and Crime dataset
(X_crime, y_crime) = load_crime_dataset()

X_train, X_test, y_train, y_test = train_test_split(X_crime, y_crime, random_state=0)
linridge = Ridge(alpha=20.0).fit(X_train, y_train)

print('Crime Dataset')
print('ridge regression linear model intercept (b): {:.3f}'.format(linridge.intercept_))
print('ridge regression linear model coeff (w): {}'.format(linridge.coef_))
print('R-squared score - training data: {:.3f}'.format(linridge.score(X_train, y_train)))
print('R-squared score - test data: {:.3f}'.format(linridge.score(X_test, y_test)))
print('Number of non-zero features: {}'.format(np.sum(linridge.coef_ != 0)))