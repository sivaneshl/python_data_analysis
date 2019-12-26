
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
matplotlib.use("Qt5Agg")

plt.figure()
data = np.random.rand(10)
plt.plot(data)
print(matplotlib.get_backend())

def onclick(event):
    plt.cla()
    plt.plot(data)
    plt.gcf().canvas.draw_idle()
    print('click event')
    plt.gca().set_title('Event at pixels {},{} \nand data {},{}'.format(event.x, event.y, event.xdata, event.ydata))

plt.gcf().canvas.mpl_connect('key_press_event', onclick)
plt.show()