import pandas as pd
import numpy as np

df = pd.DataFrame([['fname1','name1',5],
                   ['fname2','name2',8],
                   ['fname1','name1',10],
                   ['fname2','name4',3],
                   ['fname2','name6',9],
                   ['fname2','name2',19]],
                  columns=['fname','name','distance'])

print(df.groupby(by=['fname','name'])['distance'].min())