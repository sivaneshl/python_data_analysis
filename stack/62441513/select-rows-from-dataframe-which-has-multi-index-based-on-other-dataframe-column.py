import pandas as pd
import numpy as np

univer = pd.DataFrame({'State': ['Alabama', 'Alabama', 'Alabama', 'Alabama'],
                      'RegionName': ['Auburn', 'Florence', 'Jacksonville', 'Livingston']})

statbot = pd.DataFrame([['Alabama', 'Anchor Point', np.NaN, np.NaN, np.NaN],
                        ['Alabama', 'Anchorage', 296166.666667, 271933.333333, 1.089115],
                        ['Alabama', 'Fairbanks', 249966.666667, 225833.333333, 1.106863],
                        ['Alabama', 'Homer',	np.NaN, np.NaN, np.NaN],
                        ['Alabama', 'Florence', 305133.333333, 282666.666667, 1.079481],
                        ['Alabama', 'Jacksonville', np.NaN, np.NaN,  np.NaN],
                        ['Alabama', 'Ketchikan', np.NaN, np.NaN, np.NaN],
                        ['Alabama', 'KodiAlabama', np.NaN, np.NaN, np.NaN],
                        ['Alabama', 'LAlabamaes', 257433.333333, 257200.000000, 1.000907],
                        ['Alabama', 'North Pole', 241833.333333, 219366.666667, 1.102416],
                        ['Alabama', 'Palmer', 259466.666667, 263800.000000, 0.983573]],
                       columns=['State','RegionName','2008Q3','2009Q2','ratio'])

statbot = statbot.set_index(['State', 'RegionName'])
univer = univer.set_index(['State', 'RegionName'])
print(pd.merge(univer, statbot, left_index=True, right_index=True, how='inner'))