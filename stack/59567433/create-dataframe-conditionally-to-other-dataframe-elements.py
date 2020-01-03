import numpy as np
import pandas as pd

df1 = pd.DataFrame({'date':['03.05.1982','04.05.1982','05.05.1982','06.05.1982','07.05.1982','10.05.1982','11.05.1982'],
                    'A': [63.63, 64.08, 64.19, 65.11, 65.36, 65.25, 65.36],
                    'B': [63.83, 64.10, 64.19, 65.08, 65.33, 65.28, 65.36],
                    'C': [63.99, 64.22, 64.30, 65.16, 65.41, 65.36, 65.44]})

df2 = pd.DataFrame({'Name':['A','B','C'],'Notice': ['05.05.1982','07.05.1982','12.05.1982']})


# print(pd.DataFrame({'date':['03.05.1982','04.05.1982','05.05.1982','06.05.1982','07.05.1982','10.05.1982','11.05.1982'],
#                     'Result':[63.63,64.08,(64.19+64.19)/2,65.08,(65.33+65.41)/2,65.36,65.44]}))

# df3 = pd.DataFrame(columns=['date', 'Result'])
# df3['date'] = df1['date']
df3 = df1

df3['Name'] = df3.apply(lambda x: (np.where(x['date'] <= df2['Notice'])[0][0]), axis=1).apply(lambda x: df2.iloc[x]['Name'])
# df1['date'] = pd.to_datetime(df1['date'])
# df1 = df1.set_index('date')


def get_res(val, x, y):
    print(val, x, y)
    return val


df3['Result'] = df3['Name'].apply(get_res('X', df3['Name'], df3['Name'].shift(1)))


print(df3)