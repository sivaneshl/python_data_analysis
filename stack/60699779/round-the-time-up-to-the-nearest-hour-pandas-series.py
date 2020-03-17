### LIBS
from datetime import datetime, timedelta
import pandas as pd
import numpy as np


# Example Data:
observed_time = ['2020-02-20T17:54:00Z', '2020-02-20T18:54:00Z', '2020-02-21T18:54:00Z']

slice_begin_time=['2020-02-20T17:50:00Z', '2020-02-20T18:50:00Z', '2020-02-20T19:50:00Z', '2020-02-20T20:50:00Z', '2020-02-20T21:50:00Z']
slice_end_time=['2020-02-20T18:05:00Z', '2020-02-20T19:05:00Z', '2020-02-20T20:05:00Z', '2020-02-20T21:05:00Z', '2020-02-20T22:05:00Z']

def match(time):
    for i in range(len(slice_begin_time)):
        if pd.Timestamp(slice_begin_time[i]) <= time <= pd.Timestamp(slice_end_time[i]):
            return time.round('1H')
            break
    return time

s = pd.Series(pd.to_datetime(observed_time))
s = s.map(match)
print(s)

s = s.dt.round('1H')
print(s)
