import pandas as pd
import numpy as np


df = pd.DataFrame({'char':['A', 'B', 'C', 'D'],'Age':[1, 21, 19, 18],'Age1':[29, 27, 25, 26],'Age2':[60, 48, 55, 62], 'Age3':[60, 48, 55, 62],'Age4':[60, 48, 55, 62],'Age5':[18, 19, 17, 12]})


# df["Index"] = ""
# def function(df):
#     for i in range(1, len(df.columns)-2):
#         df['Index'] = np.where(df.iloc[:, 1] < 0.9 * df.iloc[:, i + 1], 'Low', 'Ok')
#
#
# function(df)

df['Index'] = df['Age'] < (df[column-1] * 0.9)

print(df)