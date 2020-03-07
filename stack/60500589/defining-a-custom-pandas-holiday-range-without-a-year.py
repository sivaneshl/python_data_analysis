import pandas as pd
import datetime
from pandas.tseries.holiday import Holiday, nearest_workday, MO

ts = pd.date_range(start='1/1/2019', freq='H', end='12/31/2019')

holidays = [Holiday('xyz', month=12, day=5),
            Holiday('July 4th', month=7, day=4, observance=nearest_workday),
            Holiday('Columbus Day', month=10, day=1, offset = pd.DateOffset(weekday=MO(2)))]


ts = pd.bdate_range(start='1/1/2019', freq='H', end='12/31/2019',
                    holidays=holidays)
print(ts)
