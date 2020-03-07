import pandas as pd
import inspect

a=[234,45,57]
b=[26,51,59]
c=[87,23,56]

def print_this(var):
    callers_local_vars = inspect.currentframe().f_back.f_locals.items()
    return (str([k for k, v in callers_local_vars if v is var][0]))

lists = [a, b, c]
fig = ['A', 'B', 'C']
cols = ['Pass_1','Pass_2','Pass_3']
df_result = pd.DataFrame(columns=cols, dtype=float)
for item in lists:
    df_result.loc[print_this(item)] = [i>0 for i in item]
print(df_result)
