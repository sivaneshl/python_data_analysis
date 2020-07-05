import pandas as pd
from datetime import datetime

df = pd.DataFrame([['2020-06-25', 303.4700, 305.26, 301.2800, 304.16, 46340400],
                   ['2020-06-24', 309.8400, 310.51, 302.1000, 304.09, 123867696],
                   ['2020-06-23', 313.4801, 314.50, 311.6101, 312.05, 68066900],
                   ['2020-06-22', 307.9900, 311.05, 306.7500, 310.62, 74007212],
                   ['2020-06-19', 314.1700, 314.38, 306.5300, 308.64, 135211345]],
                  columns=['timestamp', 'open', 'high', 'low', 'close','volume'])

df['timestamp'] = pd.to_datetime(df['timestamp'])
df.set_index('timestamp', inplace=True)

# Split data
split = len(df) - int(len(df) * 0.8)
df_train = df.iloc[split:]
df_test = df.iloc[:split]

# Normalize
from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()
df_train = df_train.values.reshape(-1,1) #df_train = scaler.fit_transform(df_train)
df_test = df_test.values.reshape(-1,1) #df_test = scaler.fit_transform(df_train)

print(df_train)
print(df_test)

# Train the Scaler with training data and smooth data
timestep = 21
for i in range(0,len(df),timestep):
    df_train = scaler.fit_transform(df_train[i:i+timestep,:])
    #train_data[di:di+smoothing_window_size,:] = scaler.transform(train_data[di:di+smoothing_window_size,:])

# You normalize the last bit of remaining data
df_test = scaler.fit_transform(df_test[i+timestep:,:])
#train_data[di+timestep:,:] = scaler.transform(train_data[di+timestep:,:])