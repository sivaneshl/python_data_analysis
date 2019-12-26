import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

iris = pd.read_csv('C:/python_data_analysis/applied_plotting_charting_and_data_representation/resources/iris.csv')
print(iris.head())

sns.pairplot(iris, hue='Name', diag_kind='kde', height=2)
# plt.show()

plt.figure(figsize=(12,8))
plt.subplot(121)
sns.swarmplot('Name', 'PetalLength', data=iris)
plt.subplot(122)
sns.violinplot('Name', 'PetalLength', data=iris)
plt.show()
