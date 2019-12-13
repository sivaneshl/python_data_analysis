import pandas as pd
import numpy as np
import decimal

def float_range(start, stop, step):
  while start < stop:
    yield float(start)
    start += decimal.Decimal(step)

base1 = pd.DataFrame({'HS CODE': [5004.0000,5005.0000,5006.0000,5007.1000,5007.2000,6115.950,6115.950,6115.960,6115.960,6115.950]})
base2 = pd.DataFrame({'HS CODE': [5004.0000,5005.0000,5006.0000,5007.1000,5007.2000],
                      '%age': 0.4})

base1 = base1.merge(base2, on=['HS CODE'], how='left')

fill_dict = dict.fromkeys(list(float_range(6110,6121,0.0001)),'0.06')

base1['%age'] = base1['%age'].fillna(base1['HS CODE'].map(fill_dict))
print(base1)
