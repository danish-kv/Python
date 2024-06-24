"""
In Python, accessor and mutator methods can be replaced with properties, which provide a more Pythonic way of
achieving the same encapsulation and validation.
"""


class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value > 0:
            self._age = value
        else:
            print("Age must be a positive number.")


person = Person('Danish', 10)

# Using properties to access and modify attributes
print(person.name)  # Output: Danish
print(person.age)  # Output: 10

person.name = 'Muhammed'
person.age = 11

print(person.name)  # Output: Muhammed
print(person.age)  # Output: 11

"""
    @property decorator is used to define getter methods.
    @<attribute>.setter decorator is used to define setter methods.
    Properties provide a more concise and Pythonic way to define accessor and mutator methods.
"""


"""
Accessor methods (getters) and mutator methods (setters) are essential in object-oriented programming to ensure 
encapsulation and controlled access to the attributes of a class. They help maintain the integrity of objects by 
providing controlled ways to retrieve and modify attribute values. In Python, properties offer a more elegant and 
Pythonic approach to implementing accessor and mutator methods.
"""
