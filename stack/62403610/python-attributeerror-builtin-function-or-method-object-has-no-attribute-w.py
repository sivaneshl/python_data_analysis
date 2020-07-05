import pandas as pd
import numpy as np
from datetime import datetime, timedelta

df = pd.DataFrame(
    {'ref': np.random.choice([0, np.nan], 20)},
    index=pd.date_range(start='2020-01-01', freq='1D', periods=20)
)

print(df)

print(df[df['ref'].isna()].index.weekofyear)


print([x.weekofyear for x, row in df[df['ref'].isna()].iterrows()])
