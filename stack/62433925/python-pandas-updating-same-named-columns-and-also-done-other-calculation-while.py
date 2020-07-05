import pandas as pd
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)

df = pd.DataFrame({'id': [1, 2, 3],
                   'col1': [350, 50, 0],
                   'col2': [350, 50, 0],
                   'col3': [350, 55, 0],
                   'col4': [350, 105, 0],
                   'col5' : [350, 50, 0],
                   'col6': [350, 0, 3495.1],
                   'col7': [350, 50, 0],
                   'col8': [350, 100, 0],
                   'col9': [350, 50, 0],
                   'col10': [350, 50, 0],
                   'col11': [0, 50, 0],
                   'col12': [0, 50, 0],
                   'col13': [0, 1025, 0],
                   'col14': [0, 1066.86, 3495.1],
                   'val_n': [3105.61, 3185.6, 3477.76]
                   })

df.set_index('id', inplace=True)
df['sum_col'] = 0
df['exceed_ind'] = 0
df['exceed_when'] = 0

for idx, row in df.iterrows():
    sum_col = 0
    exceed_ind = 0
    exceed_when = 0

    for i in range(1, 15):
        sum_col += row['col' + str(i)]

        if ((exceed_ind == 0) &
            (sum_col >= row['val_n'])):

            exceed_ind = 1
            exceed_when = i
            df.loc[idx, 'exceed_ind'] = exceed_ind
            df.loc[idx, 'exceed_when'] = exceed_when
            df.loc[idx, 'col' + str(i)] = (row['col' + str(i)] - (sum_col - row['val_n']))

        elif (exceed_ind==1) & (exceed_when < i):
            df.loc[idx, 'col' + str(i)] = 0

        df.loc[idx, 'sum_col'] = sum_col

print(df)