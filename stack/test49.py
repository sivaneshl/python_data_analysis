import pandas as pd

din=pd.DataFrame({'x':[['a','b','c'],['a','e','d', 'c']]})

din['count'] = (len(din['x']))

print(din)