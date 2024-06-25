"""
In Python, a generator is a special type of iterator that allows you to iterate over a sequence of values,
but unlike a list or other data structures, it generates the values on the fly and does not store them in memory.
This can be very memory efficient, especially when dealing with large datasets.
"""


# Generator Function
def count_up_to(max):
    count = 1
    while count <= max:
        yield count
        count += 1


counter = count_up_to(5)
print(next(counter))
print(next(counter))
print(next(counter))

"""
Generator Expression
A generator expression is similar to a list comprehension but uses parentheses instead of square brackets.
"""

square = (x * x for x in range(10))

print(next(square))  # Output: 0
print(next(square))  # Output: 1
print(next(square))  # Output: 4
print(next(square))  # Output: 9
