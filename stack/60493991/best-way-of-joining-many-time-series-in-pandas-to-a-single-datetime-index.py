import datetime as dt
import pandas as pd


csv_a = [['2019-05-25 10:00', 25, 60],
         ['2019-05-25 10:05', 26, 25],
         ['2019-05-25 10:10', 27, 63],
         ['2019-05-25 10:20', 28, 62]]
df_a = pd.DataFrame(csv_a, columns=["Timestamp", "Temperature", "Humidity"])
df_a["Timestamp"] = (pd.to_datetime(df_a["Timestamp"]))

csv_b = [['2019-05-25 10:05', 1020],
         ['2019-05-25 10:10', 1021],
         ['2019-05-25 10:15', 1019],
         ['2019-05-25 10:45', 1035]]
df_b = pd.DataFrame(csv_b, columns=["Timestamp", "Pressure"])
df_b["Timestamp"] = (pd.to_datetime(df_b["Timestamp"]))

start = dt.datetime(2019, 5, 25, 10, 0, 0)
end = dt.datetime(2019, 5, 25, 10, 20, 0)
index = pd.date_range(start, end, freq='5min')
df_c = pd.DataFrame(index=index)

print(pd.merge(df_a, df_b, how='outer').set_index('Timestamp').sort_index())