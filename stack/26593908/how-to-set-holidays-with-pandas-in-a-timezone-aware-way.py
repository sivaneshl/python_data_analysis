from pandas.tseries.holiday import Holiday, AbstractHolidayCalendar
from datetime import datetime
import pandas as pd

class ItalianHolidaysCalendar(AbstractHolidayCalendar):
    rules = [Holiday('Pasquetta', month=4, day=21),
         Holiday('Liberation day', month=4, day=25),
         Holiday('Workers day', month=5, day=1),
         Holiday('Republic day', month=6, day=2)
   ]

cal = ItalianHolidaysCalendar()

holidays_df = pd.DataFrame({})
dd = pd.date_range(datetime(2014,1,1,0), periods=24, freq='H', tz='Europe/Rome')

holidays = cal.holidays(sliceSum.datetime.min().date(), sliceSum.datetime.max().date())
for day in holidays:
    dd = dd.append(pd.date_range(day, day + pd.DateOffset(hours=23), freq='H'))

sliceSum['holiday'] = False
sliceSum.loc[sliceSum.index.isin(dd),['holiday']] = True
sliceSum[sliceSum.holiday].head(50)