import pandas as pd
import numpy as np
import calendar
import datetime

df_2019 = pd.DataFrame(np.random.rand(6, 12),
                       columns=[calendar.month_abbr[i]+'-2019' for i in range(1, 13)],
                       index=['row_name'+str(i) for i in range(1, 7)])
df_2020 = pd.DataFrame(np.random.rand(6, 12),
                       columns=[calendar.month_abbr[i]+'-2020' for i in range(1, 13)],
                       index=['row_name'+str(i) for i in range(1, 7)])
# print(df_2019)
# print(df_2020)

current_month = datetime.datetime.today().month
joined_df = pd.concat([df_2019[df_2019.columns[current_month:]], df_2020[df_2020.columns[:current_month]]], axis=1)

joined_df['garbage'] = joined_df.index=='row_name4'
print(joined_df[joined_df['garbage']==False])
