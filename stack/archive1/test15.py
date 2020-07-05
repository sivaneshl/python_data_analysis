import pandas as pd
import numpy as np

df = pd.DataFrame([['9:25:00 AM','10:58:00 AM']],
                  columns=['time1', 'time2'])

print(pd.to_datetime(df.time2)-pd.to_datetime(df.time1))
