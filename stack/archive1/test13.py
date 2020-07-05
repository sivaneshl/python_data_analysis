import pandas as pd

def generic_func(x):
    x = 'val'+str(x)
    return x

mylist=['df1','df2','df3','df4']

print({x.replace(' ', ''): pd.DataFrame([generic_func(x)]) for x in mylist})