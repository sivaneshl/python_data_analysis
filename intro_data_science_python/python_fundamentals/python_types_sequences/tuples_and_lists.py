# tuple - immutable
t = (1, 'a', 2, 'b')
print(type(t))

# lists - mutable
l = [1, 'a', 2, 'b']
print(type(l))

# loop through using for each
for item in t:
    print(item)

for item in l:
    print(item)

# loop through
i = 0
while(i != len(t)):
    print(t[i])
    i = i + 1

# arithmetic operators on lists
print(['a', 'b'] + [3, 4])
print([1, 2] * 3)

# on a tuple
t1 = (1,2,3)
t2 = (9,8)
t1 = t1 + t2
print(t1)

# 'in' operator
print(1 in [1, 2, 3])
print(5 in [1, 2, 3])
print(5 in (1, 2, 3))


# unpacking tuple
x = ('this', 'is', 'a', 'string')
first, second, third, fourth = x
print(first)
print(second, third, fourth)
