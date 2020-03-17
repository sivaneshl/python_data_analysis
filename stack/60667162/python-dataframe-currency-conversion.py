import pandas as pd
import numpy as np

df = pd.DataFrame([[55000.0,'EUR','EUR',1.195826],
                   [200000.0,'USD','USD',1.000000],
                   [130000.0,'GBP','GBP',1.324188]],
                  columns=['Salary Amount:','Salary Currency:','Country Origin:','Exchange Rate:'])

exchange_rate_GBP = df[df['Salary Currency:']=='GBP']['Exchange Rate:'].values
df['converted'] = np.where(df['Salary Currency:']!='GBP',
                           df['Salary Amount:']*exchange_rate_GBP,
                           df['Salary Amount:'])
print(df)

mean_salary_GBP = df['converted'].mean()
max_salary_GBP = df['converted'].max()
print("Mean: ", df['converted'].mean())
print("Max: ", df['converted'].max())