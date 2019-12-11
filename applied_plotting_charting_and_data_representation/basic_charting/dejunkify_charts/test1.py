import matplotlib.pyplot as plt
import numpy as np
from matplotlib.artist import Artist

plt.figure()

languages =['Python', 'SQL', 'Java', 'C++', 'JavaScript']
pos = np.arange(len(languages))
popularity = [56, 39, 34, 34, 29]

# TODO: change the bar colors to be less bright blue
# TODO: make one bar, the python bar, a contrasting color
bars = plt.bar(pos, popularity, align='center', linewidth=0, color='lightslategrey')
bars[0].set_color('#1F77B4')

# soften all labels by turning grey
plt.xticks(pos, languages, alpha=0.8)

# TODO: remove the Y label since bars are directly labeled
# plt.ylabel('% Popularity')

plt.title('Top 5 Languages for Math & Data \nby % popularity on Stack Overflow', alpha=0.8)

# TODO: remove all the ticks (both axes), and tick labels on the Y axis

plt.tick_params(top=False, bottom=False, left=False, right=False,
                labelleft=False, labelbottom=True)

# TODO: remove the frame of the chart

ax = plt.gca()
ax.spines['top'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)

# alternate way
plt.box(False)

# TODO: remove the Y label since bars are directly labeled

for bar in bars:
    plt.gca().text(bar.get_x() + bar.get_width()/2, bar.get_height() - 5, str(int(bar.get_height())) + '%',
                 ha='center', color='w', fontsize=11)
plt.show()