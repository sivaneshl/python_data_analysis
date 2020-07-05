import pandas as pd
import numpy as np

df1 = pd.DataFrame({'team': ['one', 'two', 'three', 'four', 'five'],
                    'home0-0': [86, 78, 65, 67, 100],
                    'home1-0': [76, 86, 67, 100, 0],
                    'home0-1': [91, 88, 75, 100, 67],
                    'home1-1': [75, 67, 67, 100, 100],
                    'away0-0': [57, 86, 71, 91, 50],
                    'away1-0': [73, 50, 71, 100, 100],
                    'away0-1': [78, 62, 40, 80, 0],
                    'away1-1': [50, 71, 33, 100, 0]})
df2 = pd.DataFrame({'date': ['2020-06-17', '2020-06-17', '2020-06-17', '2020-06-17', '2020-06-17', '2020-06-17', '2020-06-17'],
                    'time': [1800, 1200, 1100, 2005, 1000, 1800, 1800],
                    'team1': ['one', 'two', 'three', 'four', 'five', 'one', 'three'],
                    'team2': ['five', 'four', 'two', 'one', 'three', 'two', 'four']})

for i, row in df2.iterrows():
    team1 = df1[df1['team']==row['team1']]
    team2 = df1[df1['team']==row['team2']]
    for col in df1.columns[1:]:
        df2.loc[i, col]=(np.mean([team1[col].values[0], team2[col].values[0]]))

print(df2)
