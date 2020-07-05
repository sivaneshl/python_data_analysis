import pandas as pd

df = pd.DataFrame([['13-3-2020', 'A', 10, 15],
                   ['13-4-2020', 'A', 11, 26],
                   ['13-5-2020', 'A', 14, 14],
                   ['2-2-2018', 'B', 10, 15],
                   ['18-2-2018', 'B', 11, 26],
                   ['5-4-2018', 'B', 14, 14],
                   ['5-5-2018', 'B', 12, 12]],
                  columns=['Date', 'Product', 'Value1', 'Value2'])
df['Date'] = pd.to_datetime(df['Date'])

groups = df.groupby('Product')

for g, grp in groups:
    # print(g, grp)
    month_grp = pd.Series(pd.date_range(start=min(grp['Date']), end=max(grp['Date']), freq='MS'), name="Date").to_frame()
    new_grp = grp.append(month_grp, ignore_index=True)
    new_grp = new_grp.sort_values(by='Date').reset_index(drop=True)
    print(new_grp)
