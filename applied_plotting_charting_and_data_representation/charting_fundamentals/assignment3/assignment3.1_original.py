# Use the following data for this assignment:

import pandas as pd
import numpy as np

np.random.seed(12345)

df = pd.DataFrame([np.random.normal(32000,200000,3650),
                   np.random.normal(43000,100000,3650),
                   np.random.normal(43500,140000,3650),
                   np.random.normal(48000,70000,3650)],
                  index=[1992,1993,1994,1995])


# np.random.seed(0) makes the random numbers predictable

# >>> numpy.random.seed(0) ; numpy.random.rand(4)
# array([ 0.55,  0.72,  0.6 ,  0.54])
# >>> numpy.random.seed(0) ; numpy.random.rand(4)
# array([ 0.55,  0.72,  0.6 ,  0.54])
# With the seed reset (every time), the same set of numbers will appear every time.

# If the random seed is not reset, different numbers appear with every invocation:

# >>> numpy.random.rand(4)
# array([ 0.42,  0.65,  0.44,  0.89])
# >>> numpy.random.rand(4)
# array([ 0.96,  0.38,  0.79,  0.53])
# (pseudo-)random numbers work by starting with a number (the seed), multiplying it by a large number, then taking modulo of that product. The resulting number is then used as the seed to generate the next "random" number. When you set the seed (every time), it does the same thing every time, giving you the same numbers.

# If you want seemingly random numbers, do not set the seed. If you have code that uses random numbers that you want to debug, however, it can be very helpful to set the seed before each run so that the code does the same thing every time you run it.

# To get the most random numbers for each run, call numpy.random.seed(). This will cause numpy to set the seed to a random number obtained from /dev/urandom or its Windows analog or, if neither of those is available, it will use the clock.

import matplotlib.pyplot as plt
from matplotlib.colors import Normalize
from matplotlib.cm import get_cmap

df_mean = df.mean(axis=1)  # Averaging column entries.

# df.shape[1] gives the number of columns = 3650.
# df.std only does numerator calculation of standard deviation formula.
df_std = df.std(axis=1) / np.sqrt(df.shape[1])

# Choice of y value:
y = 37000

# In probability and statistics, 1.96 is the approximate value of the 97.5 percentile point of the normal distribution.
# 95% of the area under a normal curve lies within roughly 1.96 standard deviations of the mean, and due to the central limit theorem, this number is therefore used in the construction of approximate 95% confidence intervals.
norm = Normalize(vmin=-1.96, vmax=1.96)

# 'seismic', 'coolwarm', etc. are examples of available colour palettes.
cmap = get_cmap('coolwarm')

df_colors = pd.DataFrame([])
df_colors['intensity'] = norm(((df_mean - y) / df_std).values)  # Usual normalising formula.
df_colors['color'] = [cmap(x) for x in df_colors['intensity']]  # Assign colour depending on norm value.

# Remember we normalised df_std for assigning colour intensity earlier. Therefore the actual error will be scaled by 1.96.
# capsize sets thw whiskers for the error on the barplot.
bar_plot = plt.bar(df.index, df_mean, yerr=df_std * 1.96, color=df_colors['color'], capsize=7);

# axhline = Horizontal line.
hoz_line = plt.axhline(y=y, color='k', linewidth=2, linestyle='--');

# Text box for chosen value. 1995.5 gives the x axis location for positioning the box.
# ec is the colour of the box border. fc is the colour of the box filling.
y_text = plt.text(1995.45, y, 'y = %d' % y, bbox=dict(fc='white', ec='k'));

# Add xticks
plt.xticks(df.index, ('1992', '1993', '1994', '1995'));


# Add interactivity
def onclick(event):
    for i in range(4):
        shade = cmap(norm((df_mean.values[i] - event.ydata) / df_std.values[i]))
        bar_plot[i].set_color(shade)
    hoz_line.set_ydata(event.ydata)
    y_text.set_text('y = %d' % event.ydata);
    y_text.set_position((1995.45, event.ydata));


plt.gcf().canvas.mpl_connect('button_press_event', onclick);
plt.show()