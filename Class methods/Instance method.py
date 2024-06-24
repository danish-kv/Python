"""
Instance Methods :-
Instance methods are the most common type of methods in Python.
They operate on instances of the class and can access and modify the instance's attributes.
They are defined using the first parameter self, which represents the instance of the class.
"""

class MyClass:
    def __init__(self,value):
        self.value = value

    def increment(self):
        self.value += 1

    def display(self):
        print(f"Value : {self.value}")


obj = MyClass(10)
obj.increment()
obj.display()



"""
Instance Methods:

First parameter is self.
Can access and modify instance attributes.
Operate on instances of the class.
"""