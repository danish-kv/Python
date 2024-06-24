"""
Class Methods :-
Class methods are methods that operate on the class itself rather than instances of the class.
They cannot access or modify instance-level attributes but can access or modify class-level attributes.
They are defined using the @classmethod decorator and the first parameter cls, which represents the class itself.
"""

class MyClass:
    count = 0

    def __init__(self):
        MyClass.count += 1

    @classmethod
    def display_count(cls):
        print(f"Number of instances: {cls.count}")

obj1 = MyClass()
obj2 = MyClass()
MyClass.display_count()


"""
First parameter is cls.
Can access and modify class attributes.
Operate on the class itself.
Defined with the @classmethod decorator.
"""