import pandas as pd

df = pd.DataFrame({'list_of_value': [['a','b','c'], ['d','b','c'], ['a','b','c'], ['a','b','c']]})
s = pd.get_dummies(df.list_of_value.explode()).sum(level=0)
print(s)
print(s.dot(s.T).div(s.sum(1)))