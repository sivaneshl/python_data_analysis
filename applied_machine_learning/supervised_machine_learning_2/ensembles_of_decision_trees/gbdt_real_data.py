from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_breast_cancer

cancer = load_breast_cancer()
(X_cancer, y_cancer) = load_breast_cancer(return_X_y = True)
X_train, X_test, y_train, y_test = train_test_split(X_cancer, y_cancer, random_state=0)

clf = GradientBoostingClassifier(random_state=0).fit(X_train, y_train)
print('Breast Cancer dataset (learning_rate=0.1, max_depth=3)')
print('Accuracy for GBDT classifier using training dataset : {:.2f}'.format(clf.score(X_train, y_train)))
print('Accuracy for GBDT classifier using test dataset : {:.2f}'.format(clf.score(X_test, y_test)))

clf = GradientBoostingClassifier(learning_rate=0.01, max_depth=2, random_state=0).fit(X_train, y_train)
print('Breast Cancer dataset (learning_rate=0.01, max_depth=2)')
print('Accuracy for GBDT classifier using training dataset : {:.2f}'.format(clf.score(X_train, y_train)))
print('Accuracy for GBDT classifier using test dataset : {:.2f}'.format(clf.score(X_test, y_test)))