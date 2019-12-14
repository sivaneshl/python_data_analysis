import matplotlib.pyplot as plt
import numpy as np

fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, sharex=True)
axs = [ax1, ax2, ax3, ax4]

for n in range(len(axs)):
    sample_size = 10**(n+1)
    sample = np.random.normal(loc=0, scale=1, size=sample_size)
    axs[n].hist(sample)
    axs[n].set_title('n={}'.format(sample_size))
plt.show()

# By default, the histogram in Matplotlib uses ten bins, that is ten different bars. Here we created a shared x-axis,
# and as we sample more from the distribution, we're more likely to get outlier values further from our mean. Thus, ten
# bins for n=10 is at best capturing ten unique values, while for n=10,000, many values have to be combined into a
# single bin. Let's do the same function with the bin set to 100
