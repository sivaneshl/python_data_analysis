from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.dummy import DummyClassifier
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import confusion_matrix

dataset = load_digits()
x, y = dataset.data, dataset.target

y_binary_imbalanced = y.copy()
y_binary_imbalanced[y_binary_imbalanced != 1] = 0
X_train, X_test, y_train, y_test = train_test_split(x, y_binary_imbalanced, random_state=0)

# binary (two-class) confusion matrix
# negative class (0) is most frequent
dummy_majority = DummyClassifier(strategy='most_frequent').fit(X_train, y_train)
y_majority_predicted = dummy_majority.predict(X_test)
confusion = confusion_matrix(y_test, y_majority_predicted)
print('Most frequent class (dummy classifier)\n', confusion)

# produces random predictions with same class proportion as training set
dummy_classprop = DummyClassifier(strategy='stratified').fit(X_train, y_train)
y_classprop_predicted = dummy_classprop.predict(X_test)
confusion = confusion_matrix(y_test, y_classprop_predicted)
print('Random class-proportional prediction (dummy classifier)\n', confusion)

svm = SVC(kernel='linear', C=1, gamma='auto').fit(X_train, y_train)
y_svm_predicted = svm.predict(X_test)
confusion = confusion_matrix(y_test, y_svm_predicted)
print('Support vector machine classifier (linear kernel, C=1)\n', confusion)

logreg = LogisticRegression(max_iter=10000).fit(X_train, y_train)
y_logreg_predicted = logreg.predict(X_test)
confusion = confusion_matrix(y_test, y_logreg_predicted)
print('Logistic regression classifier (default settings)\n', confusion)

dt = DecisionTreeClassifier(max_depth=2).fit(X_train, y_train)
y_dt_predicted = dt.predict(X_test)
confusion = confusion_matrix(y_test, y_dt_predicted)
print('Decision tree classifier (max_depth = 2)\n', confusion)

