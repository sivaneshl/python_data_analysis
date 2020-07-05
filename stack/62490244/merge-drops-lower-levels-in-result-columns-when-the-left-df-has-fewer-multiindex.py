import pandas as pd

df1_columns = pd.MultiIndex.from_tuples([("A0", "B0", "C0"), ("A1", "B1", "C1")])
df1 = pd.DataFrame([[1, 2], [10, 20]], columns=df1_columns)

df2_columns = pd.MultiIndex.from_tuples([("X0", "Y0"), ("X1", "Y1")])
df2 = pd.DataFrame([[1, 200], [10, 200]], columns=df2_columns)

print(df1)
print(df2)

print(pd.merge(df2, df1, right_on=[("A0", "B0","C0")], left_on=[("X0", "Y0")], how='left'))
