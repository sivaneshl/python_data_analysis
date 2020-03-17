import pandas as pd
import matplotlib.pyplot as plt

data = pd.DataFrame([['China','Asia',2007,72.961,1318.6831,4959.11485,6539.50093],
                   ['India','Asia',2007,64.698,1110.39633,2452.21041,2722.92544],
                   ['United States','Americas',2007,78.242,301.139947,42951.6531,12934.4585],
                   ['Indonesia','Asia',2007,70.65,223.547,3540.65156,791.502035],
                   ['Brazil','Americas',2007,72.39,190.010647,9065.80083,1722.59868],
                   ['Pakistan','Asia',2007,65.483,169.270617,2605.94758,441.110355],
                   ['Bangladesh','Asia',2007,64.062,150.448339,1391.25379,209.311822],
                   ['Nigeria','Africa',2007,46.859,135.031164,2013.97731,271.9497],
                   ['Japan','Asia',2007,82.603,127.467972,31656.0681,4035.1348],
                   ['Mexico','Americas',2007,76.195,108.700891,11977.575,1301.97307]],
                  columns=['country','continent','year','lifeExpectancy','population','gdpPerCapita','GDP Billions'])
data.set_index('country', inplace=True)

ax=data[['population','gdpPerCapita']].plot(kind='bar', secondary_y='gdpPerCapita')
ax1, ax2 = plt.gcf().get_axes()
ax1.set_ylabel('Population')
ax2.set_ylabel('GDP')
# plt.legend(False)
plt.show()
