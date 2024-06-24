"""
Accessor Methods (Getter Methods)
Accessor methods, also known as getter methods, are used to fetch the value of an attribute of an object.
They provide controlled access to the attributes of a class, allowing you to retrieve the values without directly exposing the attribute itself.
Accessor methods typically do not modify the state of the object.
"""


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Accessor methods (getters)
    def get_name(self):
        return self.name

    def get_age(self):
        return self.age


person = Person('Danish', 19)

print(person.get_name())  # Output: Danish
print(person.get_age())   # Output: 19


"""
get_name() and get_age() are accessor methods.
They allow controlled access to retrieve the name and age attributes of the Person object.
"""