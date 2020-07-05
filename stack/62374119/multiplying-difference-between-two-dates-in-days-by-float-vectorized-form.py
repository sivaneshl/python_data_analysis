import pandas as pd
import numpy as np

pddt = lambda x: pd.to_datetime(x)
def cost(start_date, end_date, cost_per_day):
    start_date=pddt(start_date)
    end_date=pddt(end_date)
    total_days = (end_date-start_date) / np.timedelta64(1, 'D')
    cost = total_days * cost_per_day
    return cost

a={'start_date': ['2020-07-01','2020-07-02'], 'end_date': ['2020-07-04','2020-07-10'],'cost_per_day': [2,1.5]}
df = pd.DataFrame.from_dict(a)

costs = cost(df['start_date'], df['end_date'], df['cost_per_day'])
print(costs)
cost_adhoc = cost('2020-07-15', '2020-07-22',3)
print(cost_adhoc)