import ipympl
import matplotlib.pyplot as plt
import numpy as np

plt.figure()
data = np.random.rand(10)
plt.plot(data)

def onclick(event):
    plt.cla()
    plt.plot(data)
    plt.gca().set_title('Event at pixels {},{} \nand data {},{}'.format(event.x, event.y, event.xdata, event.ydata))

plt.gcf().canvas.mpl_connect('key_press_event', onclick)
plt.show()