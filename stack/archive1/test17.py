import pandas as pd
import numpy as np

df = pd.DataFrame([['ref1','B',20],
                   ['ref2','A',30],
                   ['ref1','B',40],
                   ['ref2','A',50],
                   ['ref1','B',60],
                   ['ref2','B',50],
                   ['ref1','B',60],
                   ['ref2','B',50],
                   ['ref1','B',60]],
                  columns=['Ref_No','Definition','Total_to_Add'])

df['answer']=df[df['Definition']=='B'].groupby(by=['Ref_No','Definition'])['Total_to_Add'].transform('sum')

df['Total_B'] = df['Definition'].eq('B').mul(df['Total_to_Add']).groupby(df['Ref_No']).transform('sum')

print(df)