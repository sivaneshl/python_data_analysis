import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

iris = pd.read_csv('C:/python_data_analysis/applied_plotting_charting_and_data_representation/resources/iris.csv')
print(iris.head())

pd.plotting.scatter_matrix(iris)
plt.show()

plt.figure()
pd.plotting.parallel_coordinates(iris, 'Name')

plt.show()