import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import mpl_toolkits.axes_grid1.inset_locator as mpl_il

normal_sample = np.random.normal(loc=0.0, scale=1.0, size=10000)
random_sample = np.random.random(size=10000)
gamma_sample = np.random.gamma(2, size=10000)

df = pd.DataFrame({'normal': normal_sample,
                   'random': random_sample,
                   'gamma': gamma_sample})
print(df.describe())

# The minimal and maximum values are showing, and there's three different percentage values. These percentage values
# make up what's called the interquartile range. There are four different quarters of the data. The first is between
# the minimal value and the first 25% of the data. And this value of 25% is called the first quartile. The second
# quarter of data is between the 25% mark and the 50% of the data. The third between 50 and 75% of the data. And 75%
# mark is called the third quartile. And the final piece of data is between the 75% and the maximum of the data.

# Like standard deviation, the interquartile range is a measure of variability of data. And it's common to plot this
# using a box plot. In a box plot, the mean, or the median, of the data is plotted as a straight line. Two boxes are
# formed, one above, which represents the 50% to 75% data group, and one below, which represents the 25% to 50% data
# group. Thin lines which are capped are then drawn out to the minimum and maximum values.

plt.figure()
plt.boxplot(df['normal'], whis='range')     # --> this gives us a basic box plot

plt.clf()   # clear current figure
plt.boxplot([df['normal'], df['random'], df['gamma']], whis='range')
ax2 = mpl_il.inset_axes(plt.gca(),  # parent axis
                        width='60%', height='40%', loc=2)
ax2.hist(df['gamma'], bins=100)
ax2.margins(x=0.5)
ax2.yaxis.tick_right()
plt.show()

# plt.figure()
# plt.hist(df['gamma'], bins=1000)
# plt.show()