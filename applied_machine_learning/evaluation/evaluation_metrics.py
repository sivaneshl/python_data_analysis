from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, classification_report
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.dummy import DummyClassifier
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier

dataset = load_digits()
x, y = dataset.data, dataset.target

y_binary_imbalanced = y.copy()
y_binary_imbalanced[y_binary_imbalanced != 1] = 0
X_train, X_test, y_train, y_test = train_test_split(x, y_binary_imbalanced, random_state=0)

dt = DecisionTreeClassifier(max_depth=2).fit(X_train, y_train)
y_dt_predicted = dt.predict(X_test)
# Accuracy = TP + TN / (TP + TN + FP + FN)
# Precision = TP / (TP + FP)
# Recall = TP / (TP + FN)  Also known as sensitivity, or True Positive Rate
# F1 = 2 * Precision * Recall / (Precision + Recall)
print('Accuracy: {:.2f}'.format(accuracy_score(y_test, y_dt_predicted)))
print('Precision: {:.2f}'.format(precision_score(y_test, y_dt_predicted)))
print('Recall Score: {:.2f}'.format(recall_score(y_test, y_dt_predicted)))
print('F1 Score: {:.2f}'.format(f1_score(y_test, y_dt_predicted)))
print('Classification Report\n', classification_report(y_test, y_dt_predicted, target_names=['not 1','1']))

dummy_classprop = DummyClassifier(strategy='stratified').fit(X_train, y_train)
y_classprop_predicted = dummy_classprop.predict(X_test)
print('Random class-proportional (dummy classifier)\n',
      classification_report(y_test, y_classprop_predicted, target_names=['not 1', '1']))

dummy_majority = DummyClassifier(strategy='most_frequent').fit(X_train, y_train)
y_majority_predicted = dummy_majority.predict(X_test)
print('Most frequent class (dummy classifier)\n',
      classification_report(y_test, y_majority_predicted, target_names=['not 1', '1']))

svm = SVC(kernel='linear', C=1, gamma='auto').fit(X_train, y_train)
y_svm_predicted = svm.predict(X_test)
print('Support vector machine classifier (linear kernel, C=1)\n',
      classification_report(y_test, y_svm_predicted, target_names=['not 1', '1']))

logreg = LogisticRegression(max_iter=10000).fit(X_train, y_train)
y_logreg_predicted = logreg.predict(X_test)
print('Logistic regression classifier (default settings)\n',
      classification_report(y_test, y_logreg_predicted, target_names=['not 1', '1']))





