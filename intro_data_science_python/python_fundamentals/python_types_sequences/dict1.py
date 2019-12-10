# Dictionaries are similar to lists and tuples in that they hold a collection of items, but they're labeled collections
# which do not have an ordering. This means that for each value you insert into the dictionary, you must also give a key
#  to get that value out. In other languages the structure is often called a map. In Python we use curly braces to denote a dictionary.

x = {'Cristiano Ronaldo' : 'cronaldo@realmadrid.com', 'Wayne Rooney' : 'wrooney@manchesterunited.com'}
print(x['Wayne Rooney'])

# add another item to the dict
x['Danielle Rossi'] = 'drossi@roma.com'
print(x)
x['Anthony Martial'] = None
print(x['Anthony Martial'])
print(x)

# iterate over the dict
for name in x:
    print(x[name])

# iterate over the values using the values() function
for name in x.values():
    print(name)

# iterate over the key and the values at once using the items() function
for name, email in x.items():
    print(name)
    print(email)



