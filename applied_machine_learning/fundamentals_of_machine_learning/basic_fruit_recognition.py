import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D

fruits = pd.read_table('../resources/fruit_data_with_colors.txt')
print(fruits.head())

lookup_fruit_name = dict(zip(fruits.fruit_label.unique(), fruits.fruit_name.unique()))
print(lookup_fruit_name)

# create train-test split
X = fruits[['mass', 'width', 'height']]
# data is usually 2-d array hence upper case X
y = fruits['fruit_label']
# labels are one-d array hence lower case y
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)
# print(X_train, X_test, y_train, y_test)

# plot a scatter plot for the training data
cmap = cm.get_cmap('gnuplot')
scatter = pd.plotting.scatter_matrix(X_train, c=y_train, marker='o', s=40,
                                     hist_kwds={'bins':15}, figsize=(12,12), cmap=cmap)
# plt.show()

# a 3-d feature scatterplot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(X_train['mass'], X_train['width'], X_train['height'], c=y_train, marker='o', s=100)
ax.set_xlabel('mass')
ax.set_ylabel('width')
ax.set_zlabel('height')
# plt.show()

# create a classifier object
from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=5)

# train the classifier (fit the estimator) using training data
print(
    knn.fit(X_train, y_train)
)

# Estimate the accuracy of the classifier on future data using the test data
print(
    knn.score(X_test, y_test)
)

# Use the trained k-NN classifier model to classify new, previously unseen objects
fruit_prediction = knn.predict([[20, 4.3, 5.5]])    # mass, width and height
print(lookup_fruit_name[fruit_prediction[0]])

fruit_prediction = knn.predict([[100, 6.3, 8.5]])    # mass, width and height
print(lookup_fruit_name[fruit_prediction[0]])

# Plot decision boundaries of the k-NN classifier
from adspy_shared_utilities import plot_fruit_knn
plot_fruit_knn(X_train, y_train, 5, 'uniform')
plot_fruit_knn(X_train, y_train, 5, 'distance')

# How sensitive is k-NN classification accuracy to the choice of the 'k' parameter?
k_range = range(1,20)
scores = []

for k in k_range:
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train, y_train)
    scores.append(knn.score(X_test, y_test))

plt.figure()
plt.xlabel('k')
plt.ylabel('accuracy')
plt.scatter(k_range, scores)
plt.xticks([0, 5, 10, 15, 20])
plt.show()


# How sensitive is k-NN classification accuracy to the train/test split proportion?
t = [0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2]

knn = KNeighborsClassifier(n_neighbors = 5)

plt.figure()

for s in t:

    scores = []
    for i in range(1,1000):
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 1-s)
        knn.fit(X_train, y_train)
        scores.append(knn.score(X_test, y_test))
    plt.plot(s, np.mean(scores), 'bo')

plt.xlabel('Training set proportion (%)')
plt.ylabel('accuracy')
plt.show()
