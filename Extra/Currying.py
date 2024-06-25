"""
Currying is a concept in functional programming where a function that takes multiple
arguments is transformed into a sequence of functions, each taking a single argument.
This technique allows you to fix some arguments of a function and produce a new function that takes the remaining arguments.
"""

"""
Without Currying
Consider a simple function that adds three numbers:
"""


def add(x, y, z):
    return x + y + z


print(add(1, 2, 3))  # Output: 6

"""
With Currying
"""
def curry_add(x):
    def inner1(y):
        def inner2(z):
            return x + y + z
        return inner2
    return inner1


add1 = curry_add(1)
add1_2 = add1(2)
result = add1_2(3)

print(result)  # Output: 6
