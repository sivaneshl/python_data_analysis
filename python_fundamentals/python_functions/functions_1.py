# add_numbers is a function that takes two numbers and adds them together.
def add_numbers(x, y):
    return x + y


print(add_numbers(1, 3))


# add_numbers updated to take an optional 3rd parameter.
# Using `print` allows printing of multiple expressions within a single cell.
def add_numbers_optional(x, y, z=None):
    if (z==None):
        return x + y
    else:
        return x + y + z


print(add_numbers_optional(1, 2, 3))
print(add_numbers_optional(1, 2))


# add_numbers updated to take an optional flag parameter.
def add_numbers_optional2(x, y, z=None, flag=False):
    if (flag):
        print('Flag is true')
    if (z==None):
        return x + y
    else:
        return x + y + z


print(add_numbers_optional2(1, 2, flag=True))


# Assign function `add_numbers` to variable `a`.
a = add_numbers(1, 4)
print(a)


# This function should add the two values if the value of the "kind" parameter is "add" or is not passed in,
# otherwise it should subtract the second value from the first.
def do_math(a, b, kind='add'):
  if (kind=='add'):
    return a+b
  else:
    return a-b

print(do_math(1, 2, 'mm'))
print(do_math(1, 2))
print(do_math(1, 2,  'add'))