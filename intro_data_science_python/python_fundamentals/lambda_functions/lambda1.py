# Lambda's are Python's way of creating anonymous functions. These are the same as other functions, but they
# have no name.The intent is that they're simple or short lived and it's easier just to write out the function in one
# line instead of going to the trouble of creating a named function.

# declare a lambda function with the word lambda followed by a list of arguments, followed by a colon and then a single expression
my_function = lambda a, b : a + b
print(my_function(1,2))