import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

np.random.seed(1234)

v1 = pd.Series(np.random.normal(0,10,100), name='v1')
v2 = pd.Series(2*v1 + np.random.normal(0,10,100), name='v2')

yticks = [10**i for i in range(2, 5)]

ax = sns.lineplot(v1, v2);
ax.set_yticks(yticks)
plt.show()