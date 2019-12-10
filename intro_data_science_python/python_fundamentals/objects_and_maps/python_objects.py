class Person:
    department = "School of Information"

    def set_name(self, new_name):
        self.name = new_name

    def set_location(self, new_location):
        self.location = new_location


person = Person()
person.set_name("Cristiano Ronaldo")
person.set_location("Italy")
print("{} lives in {} and works at {}".format(person.name, person.location, person.department))