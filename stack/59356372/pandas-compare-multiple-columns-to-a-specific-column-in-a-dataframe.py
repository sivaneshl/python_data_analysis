import pandas as pd

df = pd.DataFrame({'Product_ID': ['A', 'B', 'C'],
                   'Store_1_qty': [10, 10, 10],
                   'Store_2_qty': [20, 10, 10],
                   'Store_3_qty': [10, 10, 20]})
df['match'] = df[['Store_2_qty', 'Store_3_qty']].eq(df['Store_1_qty'],axis=0).all(1)

print(df)