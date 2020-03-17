import pandas as pd
from itertools import combinations, product


df = pd.DataFrame([['John', 10, 100],
                   ['Andrew', 5, 50],
                   ['Martha', 8, 20],
                   ['Ana', 2, 5]],
                  columns=['Col1', 'Col2', 'Col3'])

def checkRequirements(sum1, sum2):
  if sum1 == 20 and sum2 == 125:
    return True
  else:
    return False

# first check if the df as a whole satisfy the requirement
if checkRequirements(df['Col2'].sum(), df['Col3'].sum()) == True:
    print(df)
else:
    # create multiple combination of rows and drop them and check if they satisfy the requriement
    for r in range(1, len(df.index)):
        drop_list = list(combinations(list(df.index), r))
        for idx in drop_list:
            temp_df = df.drop(list(idx))
            if checkRequirements(temp_df['Col2'].sum(), temp_df['Col3'].sum()) == True:
                print(temp_df)
                break
