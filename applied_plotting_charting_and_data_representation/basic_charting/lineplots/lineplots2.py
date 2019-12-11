import numpy as np
import matplotlib.pyplot as plt
from matplotlib.artist import Artist

observation_dates = np.arange('2017-01-01', '2017-01-09', dtype='datetime64[D]')
linear_data = np.array(range(1,9))
quadratic_data = linear_data**2

# print(observation_dates,
#       linear_data,
#       quadratic_data)

def get_rc(art, depth=0):   # takes an artist and depth
    if isinstance(art, Artist):     # if the input artisit is an instance of Artist
        print(" " * depth + str(art))
        for child in art.get_children():
            get_rc(child, depth+2)


plt.figure()
plt.plot(observation_dates, linear_data, '-o',
         observation_dates, quadratic_data, '-o')

get_rc(plt.gca())

x = plt.gca().xaxis
for item in x.get_ticklabels():
    item.set_rotation(45)

plt.subplots_adjust(bottom=0.25)

ax = plt.gca()
ax.set_xlabel('Date')
ax.set_ylabel('Units')
ax.set_title('Quadratic ($x^2$) vs. Linear ($x$) Performance')

plt.show()