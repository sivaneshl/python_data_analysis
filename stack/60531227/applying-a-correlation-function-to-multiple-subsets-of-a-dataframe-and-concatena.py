import pandas as pd
from scipy.stats import spearmanr
from scipy.stats import ttest_ind

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)


df = pd.DataFrame([[100000,5,75,75,100],
                   [70000,4,55,77,80],
                   [50000,3,66,50,60],
                   [12000,1,22,60,30],
                   [35000,2,61,50,53],
                   [30000,2,66,35,77]],
                  columns=['Income','Income_Quantile','Score_1','Score_2','Score_3'])

for level in df.Income_Quantile.unique():
    # print(level)
    df_s = df.loc[df.Income_Quantile == level].drop('Income_Quantile', 1)

print(df_s)

def correlations(x,y):
    return x+y, x-y, x*y


# result = dict({key: correlations(df['Income'],val) for key, val in df[['Score_1','Score_2','Score_3']].items()})
cols = ['Score_1','Score_2','Score_3']
df_result = pd.DataFrame(columns=cols)
#                          index=['correlation','p-value','t-statistic'])

df_result.loc['t-statistic'] = [ttest_ind(df['Income'], df[x])[0] for x in cols]
df_result.loc['p-value'] = [ttest_ind(df['Income'], df[x])[1] for x in cols]
df_result.loc['correlation']= [spearmanr(df['Income'], df[x])[1] for x in cols]
print(df_result)
