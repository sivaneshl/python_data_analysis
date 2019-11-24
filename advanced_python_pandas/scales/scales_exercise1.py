import pandas as pd

s = pd.Series(['Low', 'Low', 'High', 'Medium', 'Low', 'High', 'Low'])
print(s.astype('category',
               categories=['Low', 'Medium', 'High'],
               ordered=True))

