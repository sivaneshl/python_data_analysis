import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report, precision_score, f1_score

dataset = load_digits()
x, y = dataset.data, dataset.target
X_train_mc, X_test_mc, y_train_mc, y_test_mc = train_test_split(x, y, random_state=0)

svm = SVC(kernel='linear', gamma='auto').fit(X_train_mc, y_train_mc)
svm_predicted_mc = svm.predict(X_test_mc)
confusion_mc = confusion_matrix(y_test_mc, svm_predicted_mc)
df_mc = pd.DataFrame(confusion_mc,
                     index=[i for i in range(0,10)],
                     columns=[i for i in range(0,10)])

plt.figure(figsize=(5.5,4))
sns.heatmap(df_mc, annot=True)
plt.title('SVM Linear Kernel \n Accuracy:{:.3f}'.format(accuracy_score(y_test_mc, svm_predicted_mc)))

plt.ylabel('True label')
plt.xlabel('Predicted label')

svm = SVC(kernel='rbf', gamma='auto').fit(X_train_mc, y_train_mc)
svm_predicted_mc = svm.predict(X_test_mc)
confusion_mc = confusion_matrix(y_test_mc, svm_predicted_mc)
df_mc = pd.DataFrame(confusion_mc,
                     index=[i for i in range(0,10)],
                     columns=[i for i in range(0,10)])

plt.figure(figsize=(5.5,4))
sns.heatmap(df_mc, annot=True)
plt.title('SVM RBF Kernel \n Accuracy:{:.3f}'.format(accuracy_score(y_test_mc, svm_predicted_mc)))

plt.ylabel('True label')
plt.xlabel('Predicted label')

plt.show()

print()

print(classification_report(y_test_mc, svm_predicted_mc))

print('Micro-averaged precision = {:.2f} (treat instances equally)'
      .format(precision_score(y_test_mc, svm_predicted_mc, average='micro')))
print('Macro-averaged precision = {:.2f} (treat classes equally)'
      .format(precision_score(y_test_mc, svm_predicted_mc, average='macro')))

print('Micro-averaged F1 = {:.2f} (treat instances equally)'
      .format(f1_score(y_test_mc, svm_predicted_mc, average='micro')))
print('Macro-averaged F1 = {:.2f} (treat classes equally)'
      .format(f1_score(y_test_mc, svm_predicted_mc, average='macro')))
