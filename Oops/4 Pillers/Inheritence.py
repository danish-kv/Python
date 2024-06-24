class Animal:
    def __init__(self, name):
        self.name = name


class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof..."


class Duck(Animal):
    def speak(self):
        return f"{self.name} says Quack quack..."


dog = Dog('Pinky')
duck = Duck('Ponky')
print(dog.speak())   # Pinky says Woof...
print(duck.speak())  # Ponky says Quack quack...



class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f'{self.name} is makes sound'


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def speak(self):
        return super().speak() + f", and breed is from {self.breed}"


dog = Dog('Pinky', 'Local')
print(dog.speak())  # Output : Pinky is makes sound, and breed is from Local


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

"""
Multiple Inheritance:-
Multiple inheritance allows a child class to inherit from more than one parent class
"""


class Father:
    def traits(self):
        return "Father's traits"


class Mother:
    def traits(self):
        return "Mother's traits"


class Child(Father, Mother):
    def traits(self):
        return f"{super().traits()} and Child's own traits"


child = Child()
print(child.traits())  # Output: Father's traits and Child's own traits

"""
Multilevel Inheritance:-

Multilevel inheritance allows a child class to inherit from a parent class, 
and then another child class can inherit from that child class, forming a chain
"""


class Animal:
    def speak(self):
        return "Animal speaks"


class Mammal(Animal):
    def speal(self):
        return "Mammal speaks"


class Dog(Mammal):
    def speak(self):
        return "Dog speaks"


dog = Dog()
print(dog.speak())  # Output: Dog barks

"""
Hierarchical Inheritance :-
Hierarchical inheritance allows multiple child classes to inherit from a single parent class. 
This is useful when you want to share functionality between multiple subclasses.
"""


class Animal:
    def speak(self):
        return "Animal speaks"


class Dog(Animal):
    def speak(self):
        return 'Dog barks'


class Cat(Animal):
    def speak(self):
        return 'Cat meows'


"""
5. Hybrid Inheritance
Hybrid inheritance is a combination of two or more types of inheritance.
This can involve a mix of single, multiple, multilevel, and hierarchical inheritance
"""


class Animal:
    def speak(self):
        return "Animal speaks"


class Mammal(Animal):
    def speak(self):
        return "Mammal speaks"


class Bird(Animal):
    def speak(self):
        return "Bird chirps"


class Dog(Mammal):
    def speak(self):
        return "Dog barks"


class Bat(Mammal, Bird):
    def speak(self):
        return "Bat screeches"


dog = Dog()
bat = Bat()
print(dog.speak())  # Output: Dog barks
print(bat.speak())  # Output: Bat screeches
