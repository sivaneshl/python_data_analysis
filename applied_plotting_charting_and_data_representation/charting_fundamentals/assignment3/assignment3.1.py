# Use the following data for this assignment:

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import Normalize
from matplotlib.cm import get_cmap

np.random.seed(12345)

df = pd.DataFrame([np.random.normal(32000, 200000, 3650),
                   np.random.normal(43000, 100000, 3650),
                   np.random.normal(43500, 140000, 3650),
                   np.random.normal(48000, 70000, 3650)],
                  index=[1992, 1993, 1994, 1995])

y = 40000
cmap = get_cmap('coolwarm')
norm = Normalize(vmin=-1.96, vmax=1.96)

df_mean = df.mean(axis=1)
df_std = df.std(axis=1) / np.sqrt(df.shape[1])

df_colors = pd.DataFrame([])
df_colors['depth'] = norm(((df_mean - y) / df_std).values)
df_colors['color'] = [cmap(x) for x in df_colors['depth']]

bar_plot = plt.bar(df.index, df_mean, yerr=df_std * 1.96, color=df_colors['color'], capsize=7)

hoz_line = plt.axhline(y=y, color='k', linewidth=2, linestyle='--')

y_text = plt.text(1995.45, y, 'y = %d' % y, bbox=dict(fc='white', ec='k'))
plt.xticks(df.index, df.index.values)
plt.title('Normalised Data 92-95')


def onclick(event):
    for i in range(4):
        shade = cmap(norm((df_mean.values[i] - event.ydata) / df_std.values[i]))
        bar_plot[i].set_color(shade)
    hoz_line.set_ydata(event.ydata)
    y_text.set_text('y = %d' % event.ydata)
    y_text.set_position((1995.45, event.ydata))


plt.gcf().canvas.mpl_connect('button_press_event', onclick)
plt.savefig('assignment3.png')
plt.show()
