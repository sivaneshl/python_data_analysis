import pandas as pd
import numpy as np

df = pd.read_csv('test_example.csv')

print(df.replace('None',np.NaN).groupby('id').first())

