from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_breast_cancer

cancer = load_breast_cancer()
(X_cancer, y_cancer) = load_breast_cancer(return_X_y = True)
X_train, X_test, y_train, y_test = train_test_split(X_cancer, y_cancer, random_state=0)
clf = RandomForestClassifier(max_features=8, random_state=0).fit(X_train, y_train)
print('Breast Cancer dataset')
print('Accuracy for RandomForest classifier using training dataset : {:.2f}'.format(clf.score(X_train, y_train)))
print('Accuracy for RandomForest classifier using test dataset : {:.2f}'.format(clf.score(X_test, y_test)))