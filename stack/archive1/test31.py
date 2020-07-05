import pandas as pd
import numpy as np

df1 = pd.DataFrame({'Column1': range(1,26)})
df2 = pd.DataFrame({'Column1': range(1,11),
                    'Column2': ['A','B','C','D','E','F','G','H','I','J']})

# print(df1)

df1 = df1.merge(df2, on=['Column1'], how='left')

# fill_dict = {11: 'C', 12: 'C', 13: 'C',
#              14: 'D', 15: 'D', 16: 'D', 17: 'D', 18: 'D',
#              19: 'E', 20: 'E', 21: 'E', 22: 'E', 23: 'E', 24: 'E', 25: 'E'}

# fill_dict = dict.fromkeys(range(11,14),'C')
# fill_dict.update(dict.fromkeys(range(14,19),'D'))
# fill_dict.update(dict.fromkeys(range(19,26),'E'))

fill_dict = dict([(i,'C') for i in range(11,14)] +
                 [(i,'D') for i in range(14,19)] +
                 [(i,'E') for i in range(19,26)])
# print(fill_dict)
df1['Column2'] = df1.replace({'Column1':fill_dict})
print(df1)