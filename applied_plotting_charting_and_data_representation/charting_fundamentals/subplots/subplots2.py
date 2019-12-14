import matplotlib.pyplot as plt
import numpy as np

linear_data = np.array([1,2,3,4,5,6,7,8])
exponential_data = linear_data**2

plt.figure()
ax1 = plt.subplot(1, 2, 1)  # this can also be written as plt.subplot(121)
plt.plot(linear_data, '-o')
ax2 = plt.subplot(1, 2, 2, sharey=ax1)  # sharing the same axis
plt.plot(exponential_data, '-x')
plt.show()