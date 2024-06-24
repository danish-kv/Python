"""
Static Methods:-
Static methods are methods that do not operate on an instance or the class itself.
They are defined using the @staticmethod decorator and do not take self or cls as the first parameter.
They are used to define utility functions that belong to the class but do not need to access class or instance attributes
"""

class MyClass:
    @staticmethod
    def add(a,b):
        return a + b

res = MyClass.add(10,2)
print(res)


"""
No mandatory first parameter.
Cannot access or modify instance or class attributes.
Used for utility or helper functions.
Defined with the @staticmethod decorator.
"""
