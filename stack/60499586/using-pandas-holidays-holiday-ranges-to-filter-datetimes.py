import numpy as np
import pandas as pd
import datetime
from pandas.tseries.holiday import Holiday, nearest_workday, AbstractHolidayCalendar
from dateutil.relativedelta import MO

dt = pd.date_range(start='1/1/2019', end='12/31/2019', freq='H')

class Custom_Holidays(AbstractHolidayCalendar):
    # todo: rework; Holiday object has start_date and end_date
    rules = [Holiday('Labor Day', month=9, day=1, offset=pd.DateOffset(weekday=MO(1))),
             Holiday('Independence Day', month=7, day=4)]

holiday_df = pd.date_range(start=1/1/2019, periods=24, freq='H')
holidays = Custom_Holidays().holidays(dt.min().date(), dt.max().date())

for day in holidays:
    holiday_df = holiday_df.append(pd.date_range(day, day + pd.DateOffset(hours=23), freq='H'))

# this only filters out 1 hour instead of 24 hours
# independence_day_mask = ~dt.isin(holidays.independence_day.dates(dt[0], dt[-1]))
# labor_day_mask = ~dt.isin(holidays.labor_day.dates(dt[0], dt[-1]))
#
# print(holidays.independence_day.dates(dt[0], dt[-1]))
# print(holidays.labor_day.dates(dt[0], dt[-1]))
# print(len(dt), np.sum(independence_day_mask*1))
# print(len(dt), np.sum(labor_day_mask*1))

holiday_mask = ~dt.isin(holiday_df)
print(len(dt) - np.sum(holiday_mask*1))