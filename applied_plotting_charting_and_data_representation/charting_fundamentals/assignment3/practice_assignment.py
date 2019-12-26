import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# generate 4 random variables from the random, gamma, exponential, and uniform distributions
n = 100
x1 = np.random.normal(-2.5, 1, n)
x2 = np.random.gamma(2, 1.5, n)
x3 = np.random.exponential(2, n)+7
x4 = np.random.uniform(14,20, n)

fig, ((ax1, ax2, ax3, ax4)) = plt.subplots(1, 4, sharey=True)
# , sharex=True, sharey=True)

axs = [ax1, ax2, ax3, ax4]
xs = [x1, x2, x3, x4]
titles = ['Normal', 'Gamma', 'Exponential', 'Uniform']
colors = ['blue', 'green', 'red', 'yellow']
axiss = [[-7.5, 2.5, 0, 0.6], [0, 10, 0, 0.6], [7, 17, 0, 0.6], [12, 22, 0, 0.6]]
# plt.gca().set_xlim(-10, 25)
# plt.gca().set_ylim(0, 0.6)
# plt.axis([-10, 25, 0, 0.6])


def fnupdate(curr):

    if curr == n:
        a.event_source.stop()

    for i in range(len(axs)):
        axs[i].cla()
        axs[i].hist(xs[i][:curr], density=True, bins=20, alpha=0.5, color=colors[i])
        axs[i].set_title('{} - n={}'.format(titles[i],curr))
        axs[i].axis(axiss[i])
        # axs[i].spines['right'].set_visible(False)
        # axs[i].spines['left'].set_visible(False)
        # axs[i].spines['top'].set_visible(False)

a = animation.FuncAnimation(fig, fnupdate, interval=50)
plt.show()
