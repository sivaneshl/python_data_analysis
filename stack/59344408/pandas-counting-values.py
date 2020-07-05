import pandas as pd
from io import StringIO

data = """
ID,Season
A,Winter
A,Summer
B,Summer
C,Winter
C,Summer
D,Summer
D,Summer
E,Winter
"""

df = pd.read_csv(StringIO(data),sep=',')
df_both = df.groupby(['ID','Season'])['ID'].count().unstack().fillna(0)
print (len(df_both.loc[(df_both['Summer'] > 0) & (df_both['Winter'] > 0)]) / len(df))