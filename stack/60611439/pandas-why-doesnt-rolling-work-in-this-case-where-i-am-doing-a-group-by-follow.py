import pandas as pd
import numpy as np

df = pd.DataFrame({'B': [0, 1, 2, np.nan, 4, 10], "id" : [1,1,1,2,2,2]},
                  index = [pd.Timestamp('20130101 00:00:00'),
                           pd.Timestamp('20130201 00:00:00'),
                           pd.Timestamp('20130301 00:00:00'),
                           pd.Timestamp('20130301 00:00:00'),
                           pd.Timestamp('20130401 00:00:00'),
                           pd.Timestamp('20130501 00:00:00')])


print(df.groupby("id").rolling("2M").agg(["mean"]))