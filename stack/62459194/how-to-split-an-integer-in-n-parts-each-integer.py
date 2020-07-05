import pandas as pd

df = pd.DataFrame({'Date': pd.date_range('2019-09-18', '2019-09-30'),
                   'Desciption': ['A','A','A','A','A','A','A','A','A','A','A','A','A'],
                   'qty': [6,6,6,6,5,5,5,5,5,5,5,5,5],
                   'flag': [3,3,3,3,7,7,7,7,7,7,7,7,7],
                   'count': [4,4,4,4,9,9,9,9,9,9,9,9,9]})

def get_split(x, n):
    # if x is greater than n, then we have to split x, x times which is all 1s
    # and fill 0s the remaining n-x times
    if x < n:
        return [1]*x + [0]*(n-x)

    q = x//n    # quotient
    r = x%n     # reminder
    c = n-r     #
    if r == 0:
        return [q]*n
    else:
        return [q+1 if i>=c else q for i in range(n)]

df['new qty'] = 0
groups = df.groupby('flag')
for key, grp in groups:
    x, n = grp.head(1)[['qty', 'count']].values[0]
    splits = sorted(get_split(x, n), reverse=True)
    j=0
    for i, row in grp.iterrows():
        df.loc[i, 'new qty'] = splits[j]
        j+=1

print(df)