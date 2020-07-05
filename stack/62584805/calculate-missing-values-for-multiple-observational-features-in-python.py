import numpy as np
import pandas as pd

df = pd.DataFrame(np.array([['1', '50', 'normal'], ['1', '57', 'csection'],
                            ['2', '73', 'normal'], ['2', None, 'normal'], ['2', None, 'ventouse']]),
                  columns=['id', 'weight', 'route'])


print(df)
missing_values = df.isna().mean().round(4) * 100
print(missing_values)
