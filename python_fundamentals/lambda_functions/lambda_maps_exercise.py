people = ['Dr. Christopher Brooks', 'Dr. Kevyn Collins-Thompson', 'Dr. VG Vinod Vydiswaran', 'Dr. Daniel Romero']


def split_title_and_name(person):
    return person.split()[0] + ' ' + person.split()[-1]


# option 1 - using the lambda function version of split_title_and_name
for person in people:
    print(split_title_and_name(person) == (lambda x: x.split()[0] + ' ' + x.split()[-1])(person))

# option 2 - using a map function as a lambda function
print(list(map(split_title_and_name,people)) == list(map(lambda person: person.split()[0] + ' ' + person.split()[-1], people)))