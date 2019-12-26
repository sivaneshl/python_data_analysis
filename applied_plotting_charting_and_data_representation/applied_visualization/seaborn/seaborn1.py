import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

np.random.seed(1234)

v1 = pd.Series(np.random.normal(0,10,1000), name='v1')
v2 = pd.Series(2*v1 + np.random.normal(60,15,1000), name='v2')

plt.figure()
plt.hist(v1, alpha=0.7, bins=np.arange(-50, 150, 5), label='v1')
plt.hist(v2, alpha=0.7, bins=np.arange(-50, 150, 5), label='v2')
plt.legend()

# plt.show()

plt.figure()
plt.hist([v1,v2], histtype='bar', stacked=True, density=True);
v3 = np.concatenate((v1,v2))
print(v3)
sns.kdeplot(v3);
# plt.show()


plt.figure()
sns.distplot(v3, hist_kws={'color':'Teal'}, kde_kws={'color': 'Navy'})
# plt.show()

sns.jointplot(v1, v2, alpha=0.5)
# plt.show()

grid = sns.jointplot(v1, v2, alpha=0.5)
grid.ax_joint.set_aspect('equal')
# plt.show()

sns.jointplot(v1, v2, kind='hex')
# plt.show()

sns.set_style('white')
sns.jointplot(v1, v2, kind='kde',shape=0)
plt.show()


