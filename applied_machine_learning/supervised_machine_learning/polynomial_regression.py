# Polynomial regression

from sklearn.linear_model import LinearRegression, Ridge
from sklearn.preprocessing import PolynomialFeatures
from sklearn.datasets import make_friedman1
from sklearn.model_selection import train_test_split

X_F1, y_F1 = make_friedman1(n_samples=100, n_features=7, random_state=0)

X_train, X_test, y_train, y_test = train_test_split(X_F1, y_F1, random_state=0)
linreg = LinearRegression().fit(X_train, y_train)
print('Linear model coeff (w): {}'.format(linreg.coef_))
print('Linear model intercept (b): {:.3f}'.format(linreg.intercept_))
print('R-squared score training: {:.3f}'.format(linreg.score(X_train, y_train)))
print('R-squared score test: {:.3f}'.format(linreg.score(X_test, y_test)))

print('\nNow we transform the original input data to add\n\
polynomial features up to degree 2 (quadratic)\n')
poly = PolynomialFeatures(degree=2)
X_F1_Poly = poly.fit_transform(X_F1)
X_train, X_test, y_train, y_test = train_test_split(X_F1_Poly, y_F1, random_state=0)
linreg = LinearRegression().fit(X_train, y_train)
print('(poly degree 2)Linear model coeff (w): {}'.format(linreg.coef_))
print('(poly degree 2)Linear model intercept (b): {:.3f}'.format(linreg.intercept_))
print('(poly degree 2)R-squared score training: {:.3f}'.format(linreg.score(X_train, y_train)))
print('(poly degree 2)R-squared score test: {:.3f}'.format(linreg.score(X_test, y_test)))

print('\nAddition of many polynomial features often leads to\n\
overfitting, so we often use polynomial features in combination\n\
with regression that has a regularization penalty, like ridge\n\
regression.\n')
X_train, X_test, y_train, y_test = train_test_split(X_F1_Poly, y_F1, random_state=0)
linreg = Ridge().fit(X_train, y_train)
print('(poly degree 2 + ridge)Linear model coeff (w): {}'.format(linreg.coef_))
print('(poly degree 2 + ridge)Linear model intercept (b): {:.3f}'.format(linreg.intercept_))
print('(poly degree 2 + ridge)R-squared score training: {:.3f}'.format(linreg.score(X_train, y_train)))
print('(poly degree 2 + ridge)R-squared score test: {:.3f}'.format(linreg.score(X_test, y_test)))


