from sklearn.datasets import load_digits
from sklearn.model_selection import cross_val_score
from sklearn.svm import SVC

dataset = load_digits()
X, y = dataset.data, dataset.target == 1
clf = SVC(C=1, kernel='linear', gamma='auto')

# accuracy is the default scoring metric
print('Cross validation (accuracy):', cross_val_score(clf, X, y, cv=5))
# use AUC as scoring metric
print('Cross validation (AUC):', cross_val_score(clf, X, y, cv=5, scoring='roc_auc'))
# use recall as scoring metric
print('Cross validation (recall)', cross_val_score(clf, X, y, cv=5, scoring='recall'))

