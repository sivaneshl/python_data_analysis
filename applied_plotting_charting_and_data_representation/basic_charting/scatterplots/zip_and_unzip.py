# zip
zip_generator = zip([1,2,3,4,5],[6,7,8,9,10])
print(list(zip_generator))

# unpacking zip
zip_generator = zip([1,2,3,4,5],[6,7,8,9,10])
x, y = zip(*zip_generator)
print(x)
print(y)