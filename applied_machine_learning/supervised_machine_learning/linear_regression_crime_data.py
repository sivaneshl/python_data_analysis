from applied_machine_learning.fundamentals_of_machine_learning.adspy_shared_utilities import load_crime_dataset
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Communities and Crime dataset
(X_crime, y_crime) = load_crime_dataset()

X_train, X_test, y_train, y_test = train_test_split(X_crime, y_crime, random_state=0)
linreg = LinearRegression().fit(X_train, y_train)

print('Crime dataset')
print('linear model coef (w): {}'.format(linreg.coef_))
print('linear model intercept (b): {:.3f}'.format(linreg.intercept_))
print('R-squared score on training data: {:.3f}'.format(linreg.score(X_train, y_train)))
print('R-squared score on test data: {:.3f}'.format(linreg.score(X_test, y_test)))

# plotting
plt.figure()
plt.scatter(X_crime['population'], y_crime, marker='o', s=50, alpha=0.5)
plt.plot(X_crime['population'], (linreg.coef_[0] * X_crime['population']) + linreg.intercept_, 'r-')
plt.title('Least-squares linear regression')
plt.xlabel('Feature value (x) - Population')
plt.ylabel('Target value (y)')
plt.show()
