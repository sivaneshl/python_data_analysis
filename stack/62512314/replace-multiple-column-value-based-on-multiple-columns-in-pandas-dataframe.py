import pandas as pd

df = pd.DataFrame({'name': [1, 1, 2, 2, 3, 3],
                   'city': ['A', 'A', 'A', 'A', 'B', 'B'],
                   'kpi': ['X', 'Y', 'X', 'Y', 'X', 'Y'],
                   '01-Jan-20': [9, 120, 10, 1, 1, 2],
                   '02-Jan-20': [9, 120, 20, 0, 2, 100],
                   '03-Jan-20': [0, 0, 10, 11, 3, 5],
                   'SD': [0, 0, 10, 6.08276253, 1, 55.73448962],
                   'Mean': [9, 120, 20, 4, 2, 35.66666667]})
print(df)

def indicator(kpi_value, kpi_std, kpi_mean ):
    SD_distance = abs((kpi_mean-kpi_value)/kpi_std) if kpi_std>0 else (kpi_mean-kpi_value)
    if SD_distance >=1.5:
        return -1
    else:
        return 1

date_cols = df.iloc[:,3:-2].columns
for col in date_cols:
    df[col] = df.apply(lambda x: indicator(x[col], x["SD"], x["Mean"]), axis=1)

print(df)
