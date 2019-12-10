import matplotlib.pyplot as plt
from matplotlib.artist import Artist

zip_generator = zip([1,2,3,4,5], [6,7,8,9,10])
x, y = zip(*zip_generator)

plt.figure()
plt.scatter(x[:2], y[:2], c='blue', label='Tall Students')
plt.scatter(x[2:], y[2:], c='red', label='Short Students')
plt.xlabel('The number of times  the child kicked the ball')
plt.ylabel('The grade of the student')
plt.title('Relationship between ball kicking and grades')
plt.legend()    # by default placed in the upper left hand corner
plt.legend(loc=4, frameon=False, title='Legend')
legend = plt.gca().get_children()[-2]

print(legend.get_children()[0].get_children()[1].get_children()[0].get_children())

def get_rc(art, depth=0):   # takes an artist and depth
    if isinstance(art, Artist):     # if the input artisit is an instance of Artist
        print(" " * depth + str(art))
        for child in art.get_children():
            get_rc(child, depth+2)
get_rc(legend)


plt.show()


