import pandas as pd
import datetime

r = list(pd.Series([datetime.time(6, 59), datetime.time(7, 7), datetime.time(7, 12), datetime.time(7, 16), datetime.time(7, 18), datetime.time(7, 22), datetime.time(7, 27), datetime.time(7, 31), datetime.time(7, 37), datetime.time(7, 43)]))
j = list(pd.Series([datetime.time(6, 58, 16), datetime.time(7, 6, 17), datetime.time(7, 11, 32), datetime.time(7, 15, 30), datetime.time(7, 17, 4), datetime.time(7, 22, 13), datetime.time(7, 27, 8), datetime.time(7, 31, 26), datetime.time(7, 37, 26), datetime.time(7, 44)]))

print([(datetime.datetime.combine(datetime.date.today(),rx)-datetime.datetime.combine(datetime.date.today(),jx)).total_seconds()/60
       for rx, jx in zip(r,j)])

