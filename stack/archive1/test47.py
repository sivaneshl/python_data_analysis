import pandas as pd

index1 = pd.IntervalIndex.from_tuples([(1, 3), (2.5, 4), (6, 7)])
x = pd.Series([1, 2, 3], index=index1)

index2 = pd.IntervalIndex.from_tuples([(1, 2), (5, 6.5)])
y = pd.Series([10, 20], index=index2)

# z = pd.concat([x,y])
# index3 = pd.interval_range(start=0,end=6.5,freq=0.5)
z = x + y
# z.index=index3
print(z)
print(z.index.values)