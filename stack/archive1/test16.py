import pandas as pd
import numpy as np

df = pd.DataFrame([["a", "d"], ["", ""], ["", "3"]],
            columns=["a", "b"])

df['c']=np.where(df['a']!='',df['a'] + '()' + df['b'],'')
print(df)