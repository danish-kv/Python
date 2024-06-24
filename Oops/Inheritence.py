# class Animal:
#     def __init__(self, name):
#         self.name = name
#
#
# class Dog(Animal):
#     def speak(self):
#         return f"{self.name} says Woof..."
#
#
# class Duck(Animal):
#     def speak(self):
#         return f"{self.name} says Quack quack..."
#
#
# dog = Dog('Pinky')
# duck = Duck('Ponky')
# print(dog.speak())
# print(duck.speak())
#


# class Animal:
#     def __init__(self, name):
#         self.name = name
#
#     def speak(self):
#         return f'{self.name} is makes sound'
#
#
# class Dog(Animal):
#     def __init__(self, name, breed):
#         super().__init__(name)
#         self.breed = breed
#
#     def speak(self):
#         return super().speak() + f", and breed is from {self.breed}"
#
#
# dog = Dog('Pinky', 'Local')
# print(dog.speak())


"""
Single Inheritance:-
Single inheritance allows a child class to inherit from a single parent class.
"""


class Animal:
    def speak(self):
        return 'Animal Speaks'


class Dog:
    def speak(self):
        return 'Dog barks'


dog = Dog()
print(dog.speak())  # Output: Dog barks


class Father:
    def traits(self):
        return "Father's traits"


class Mother:
    def traits(self):
        return "Mother's traits"


class Child(Father,Mother):
    def traits(self):
        return f"{super().traits()} and Child's own traits"


child = Child()
print(child.traits())  # Output: Father's traits and Child's own traits
