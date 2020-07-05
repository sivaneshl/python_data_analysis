import pandas as pd

days_predicted = 5
rng = pd.date_range(group_by_df['day'].min(), periods=len(group_by_df) + days_predicted, freq='D')
df = pd.DataFrame({'day': rng})
df[sensor_name] = group_by_df["o3"] #the current existent values for o3
df[sensor_name][len(group_by_df):] = "" #the future values