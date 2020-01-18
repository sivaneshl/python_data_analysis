from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_breast_cancer

cancer = load_breast_cancer()
(X_cancer, y_cancer) = load_breast_cancer(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X_cancer, y_cancer, random_state=0)
clf = LogisticRegression(C=1, max_iter=10000).fit(X_train, y_train)

print('Training dataset accuracy: {:.3f}'.format(clf.score(X_train, y_train)))
print('Testing dataset accuracy: {:.3f}'.format(clf.score(X_test, y_test)))


