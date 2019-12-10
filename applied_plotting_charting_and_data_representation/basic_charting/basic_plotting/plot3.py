import matplotlib.pyplot as plt

plt.figure()
plt.plot(3, 2, '.')
ax = plt.gca()  # get current axes
ax.axis([0, 6, 0, 10])  # set the axis with [min x, max x, min y, max y]
plt.show()

plt.figure()
plt.plot(1.5, 1.5, '.')
plt.plot(2, 2, '.')
plt.plot(2.5, 2.5, '.')
plt.show()

# get all the child objects that athe axes contains
ax = plt.gca()
print(ax.get_children())