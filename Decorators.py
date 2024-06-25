"""
Decorators in Python are a powerful and convenient way to modify the behavior of a function or a class method. They
allow you to wrap another function in order to extend or alter its behavior without permanently modifying it.
"""

"""
Basic Concept A decorator is a function that takes another function as an argument and returns a new function that 
typically extends the behavior of the original function. Decorators are applied using the @decorator_name syntax 
above the function to be decorated.
"""


def decorator(func):
    def wrapper():
        res = func()
        return res.upper()

    return wrapper


@decorator
def hello():
    return 'hello'


print(hello())


def repeat(till):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(till):
                func(*args, **kwargs)

        return wrapper

    return decorator


@repeat(3)
def greet(name):
    print(f'Hello {name}')


greet('Danish')
