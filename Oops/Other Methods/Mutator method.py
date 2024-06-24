"""
Mutator Methods (Setter Methods):-
Mutator methods, also known as setter methods, are used to modify the values of
attributes of an object. They provide controlled means to change the state or update the values of attributes,
often with validation or additional logic to ensure the object's integrity.
"""

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def set_name(self, name):
        self.name = name

    def set_age(self,age):
        if age > 0:
            self.age = age
        else:
            print("Age must be a positive number.")


person = Person("danish", 19)

person.set_name('muhammed')
person.set_age(20)


"""
set_name() and set_age() are mutator methods.
They allow controlled modification of the name and age attributes of the Person object.
set_age() includes validation logic to ensure that the age is a positive number.
"""