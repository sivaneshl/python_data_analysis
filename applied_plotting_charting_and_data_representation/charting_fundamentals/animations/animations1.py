import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

n = 100
x = np.random.randn(n)
print(x)

def fnupdate(curr):
    if curr == n:
        a.event_source.stop()

    plt.cla()
    bins = np.arange(-4, 4, 0.5)
    plt.hist(x[:curr], bins=bins)
    plt.axis([-4, 4, 0, 30])
    plt.gca().set_title('Sampling the Normal Distribution')
    plt.gca().set_xlabel('Value')
    plt.gca().set_ylabel('Frequenny')
    plt.annotate('n={}'.format(curr), [3,27])

fig = plt.figure()
a = animation.FuncAnimation(fig, fnupdate, interval=100)
plt.show()

