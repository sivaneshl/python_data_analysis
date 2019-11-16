import datetime as dt
import time as tm

# print time object --> float since epoc 01/01/1970
print(tm.time())

# convert to datetime
dtnow = dt.datetime.fromtimestamp(tm.time())
print(dtnow)

# print date components
print(dtnow.year, dtnow.month, dtnow.day, dtnow.hour, dtnow.minute, dtnow.second)
# print as a list
print([dtnow.year, dtnow.month, dtnow.day, dtnow.hour, dtnow.minute, dtnow.second])

# time deltas
delta = dt.timedelta(days = 100)
print(delta)
today = dt.date.today()
print(today)
print(today-delta)
print(today > today-delta)
