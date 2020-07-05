import pandas as pd

df = pd.DataFrame({'Age': [23, 39, 70, 41, 50, 17, 29],
                   'Predict': [0, 0, 0, 1, 0, 0 ,1]})
data = df.sort_values(by='Age')

for i, grp in data.groupby([(data['Predict'] != data['Predict'].shift()).cumsum()]):
    print('group', i)
    print(grp)