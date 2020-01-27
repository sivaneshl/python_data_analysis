import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_digits
from sklearn.svm import SVC
from sklearn.dummy import DummyClassifier

dataset = load_digits()
x, y = dataset.data, dataset.target

for class_name, class_count in zip(dataset.target_names, np.bincount(dataset.target)):
    print(class_name, class_count)

y_binary_imbalanced = y.copy()
y_binary_imbalanced[y_binary_imbalanced != 1] = 0
print('Original dataset:', y[1:30])
print('New binary labels:', y_binary_imbalanced[1:30])
print(np.bincount(y_binary_imbalanced))

X_train, X_test, y_train, y_test = train_test_split(x, y_binary_imbalanced, random_state=0)
svm = SVC(kernel='rbf', C=1, gamma='auto').fit(X_train, y_train)
print(svm.score(X_test, y_test))

## Dummy classifier
dummy_majority = DummyClassifier(strategy='most_frequent').fit(X_train, y_train)
y_dummy_predictions = dummy_majority.predict(X_test)
print(y_dummy_predictions)
print(dummy_majority.score(X_test, y_test))
# Compare against svm
svm = SVC(kernel='linear', C=1, gamma='auto').fit(X_train, y_train)
print(svm.score(X_test, y_test))

