"""
Context Managers:- context manager is a Python object that provides a way to manage resources, such as opening and
closing files, acquiring and releasing locks, or connecting to databases. It allows you to allocate and release
resources precisely when you want to, without relying on Python's garbage collection mechanism
"""


"""

Basics of Context Managers:

1. Using with Statement:
    The primary mechanism for working with context managers in Python is the with statement.
    It ensures that resources are properly managed by invoking the context manager's methods (__enter__ and __exit__) 
    automatically before and after the block of code inside the with statement.

2. __enter__ Method:
    Defined by the context manager, the __enter__ method sets up the necessary resources or prepares the environment.
    It is called when execution enters the with statement block.

3. __exit__ Method:
    Also defined by the context manager, the __exit__ method is responsible for cleaning up resources or handling exceptions.
    It is called when execution leaves the with statement block, even if an exception occurs within the block.

"""


# Using a context manager to open and read a file
with open('example.txt', 'r') as f:
    contents = f.read()
    print(contents)
# File is automatically closed at the end of the 'with' block
