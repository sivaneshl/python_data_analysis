from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

dataset = load_digits()
x, y = dataset.data, dataset.target

y_binary_imbalanced = y.copy()
y_binary_imbalanced[y_binary_imbalanced != 1] = 0
X_train, X_test, y_train, y_test = train_test_split(x, y_binary_imbalanced, random_state=0)

lr = LogisticRegression(max_iter=10000).fit(X_train, y_train)
y_scores_lr = lr.fit(X_train, y_train).decision_function(X_test)
y_score_list = list(zip(y_test[:20], y_scores_lr[:20]))
print(y_score_list)

y_proba_lr = lr.fit(X_train, y_train).predict_proba(X_test)
y_proba_list = list(zip(y_test[:20], y_proba_lr[:20, 1]))
print((y_proba_list))
