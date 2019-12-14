import matplotlib.pyplot as plt
import numpy as np

linear_data = np.arange(1,9)

fig, ((ax1, ax2, ax3), (ax4, ax5, ax6), (ax7, ax8, ax9)) = plt.subplots(3, 3,
                                                                        sharex=True,
                                                                        sharey=True)
ax5.plot(linear_data, '-')
# plt.show()

# to display the x ticks and y ticks for all the sub plots
for ax in plt.gcf().get_axes():
    for label in ax.get_xticklabels() + ax.get_yticklabels():
        label.set_visible(True)
plt.show()


