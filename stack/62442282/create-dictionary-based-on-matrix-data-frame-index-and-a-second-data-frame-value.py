import pandas as pd

df = pd.read_csv("Example.csv", header=0, index_col="Forest")
df2 = pd.read_csv("ExampleSupply.csv", header=0, index_col="Forest")

I = df.index.tolist()

dQ = {}
for forest in I:
    dQ[forest] = df2.loc[forest]['Supply']
print(dQ)

dQ1 = {forest: df2.loc[forest]['Supply'] for forest in I}
print(dQ1)

print(df2.to_dict()['Supply'])