import matplotlib.pyplot as plt
import numpy as np

fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, sharex=True)
axs = [ax1, ax2, ax3, ax4]

for n in range(len(axs)):
    sample_size = 10**(n+1)
    sample = np.random.normal(loc=0, scale=1, size=sample_size)
    axs[n].hist(sample, bins=100)   # setting the bin size for the histogram as 100
    axs[n].set_title('n={}'.format(sample_size))
plt.show()