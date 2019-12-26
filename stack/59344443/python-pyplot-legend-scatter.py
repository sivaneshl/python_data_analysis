import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import ListedColormap

x = [1, 3, 4, 6, 7, 9]
y = [0, 0, 5, 8, 8, 8]
labels = ['A', 'B', 'C']
colors = [0, 0, 1, 2, 2, 2]
scatter = plt.scatter(x, y, c=colors, cmap='viridis')
plt.legend(handles=scatter.legend_elements()[0], labels=labels)
plt.savefig('fig.png')
plt.show()