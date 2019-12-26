import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# print(plt.style.available)
plt.style.use('seaborn-colorblind')

np.random.seed(123)
df = pd.DataFrame({'A': np.random.randn(365).cumsum(0),
                   'B': np.random.randn(365).cumsum(0) + 20,
                   'C': np.random.randn(365).cumsum(0) - 20},
                  index=pd.date_range('1/1/2017', periods=365))

print(df.head())
df.plot()
# plt.show()

df.plot('A', 'B', kind='scatter')
# plt.show()

df.plot.scatter('A', 'C', c='B', s=df['B'], colormap='viridis')
# plotting the values of A and C column with the color and size changing based on the value of B column
# plt.show()

ax = df.plot.scatter('A', 'C', c='B', s=df['B'], colormap='viridis')
ax.set_aspect('equal')
# plt.show()

df.plot.box()
# plt.show()

df.plot.hist(alpha=0.5)
# plt.show()

df.plot.kde()   # density estimation
plt.show()
