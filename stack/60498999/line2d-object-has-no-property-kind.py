import pandas as pd
import matplotlib.pyplot as plt

data = pd.DataFrame({'Time': ['2009-04-01 00:00:00', '2009-01-01 03:00:00', '2009-01-01 06:00:00',
                              '2009-05-01 09:00:00', '2013-01-01 15:00:00', '2013-01-01 18:00:00',
                              '2013-06-01 21:00:00', '2013-01-02 00:00:00'],
                     'L06_347': [0.137417, 0.13125, 0.1135, 0.13575, 1.42, 1.178583, 0.89825, 0.86],
                     'LS06_347': [0.0975, 0.088833, 0.09125, 0.0915, 1.42, 1.178583, 0.89825, 0.86],
                     'LS06_348': [0.016833, 0.016417, 0.01675, 0.01625, 0.096333, 0.083083, 0.077167, 0.075]})
data['Time'] = pd.to_datetime(data['Time'])
data.set_index(['Time'], inplace=True)

print(data[data.index.month.isin([4,5,6])])

# fig,ax = plt.subplots(1)
# ax = data['2013'].mean().plot(kind='bar')
# ax.set_xlabel('x label name')   # replace with the labels you want
# ax.set_ylabel('Mean')
# plt.xticks(rotation=30)
# plt.show()