import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.style
import matplotlib.font_manager

data = pd.read_csv('error_data')

size = list(data['size'])
x = data['x']
y = data['y']
error = data['error']
print(size)

plot_xy = plt.scatter(x, y ,s=20,c=size, alpha=0.5)
colors = plt.colorbar(plot_xy)
size_colors = mpl.colors.to_rgba(size)
for x, y, e, color in zip(x, y, error ,colors):
    plt.errorbar(x, y, e, lw=1, capsize=3, color=color, alpha=0.5)
plt.show()