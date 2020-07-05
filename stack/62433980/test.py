import pandas as pd
import numpy as np

data1 = pd.DataFrame({
    'DATAMECI': ['17/06/2020', '17/06/2020'],
    'ORAMECI': ['11:30', '15:30'],
    'TXTECHIPA1': ['Everton', 'Man City'],
    'TXTECHIPA2': ['Hull', 'Leeds']})
data2 = pd.DataFrame({
    'Team': ['Hull', 'Leeds','Everton', 'Man City'],
    'Home0-0': ['80', '78','80', '66'],
    'Home1-0': ['81', '100','90', '70'],
    'Away0-1': ['88', '42','75', '69']})

for i, row in data1.iterrows():
    team1 = data2[data2['Team']==row['TXTECHIPA1']]
    team2 = data2[data2['Team']==row['TXTECHIPA2']]
    for col in data2.columns[1:]:
        data1.loc[i, col]=(np.mean([int(team1[col].values[0]), int(team2[col].values[0])]))

print(data1)
