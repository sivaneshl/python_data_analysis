import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(123)
df1 = pd.DataFrame({'A': np.random.randn(365).cumsum(0)}, index=pd.date_range('1/1/2017', periods=365))
df2 = pd.DataFrame({'A': np.random.randn(365).cumsum(0)}, index=pd.date_range('1/1/2017', periods=365))
df3 = pd.DataFrame({'A': np.random.randn(365).cumsum(0)}, index=pd.date_range('1/1/2017', periods=365))
df4 = pd.DataFrame({'A': np.random.randn(365).cumsum(0)}, index=pd.date_range('1/1/2017', periods=365))


fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, sharex=True)
axs = [ax1, ax2, ax3, ax4]
dfs = [df1, df2, df3, df4]

for n in range(len(axs)):
    axs[n].hist(dfs[n]['A'], bins=50)
plt.show()

# hist_1 = df1.hist(bins=50,range=[0,1])
# hist_2 = df2.hist(bins=50,range=[0,1])
# hist_3 = df3.hist(bins=50,range=[0,1])
# hist_4 = df4.hist(bins=50,range=[0,1])
# plt.show()
