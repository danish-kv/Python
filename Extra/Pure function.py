"""
 Pure function is a function that, given the same input, will always return the same output and does not produce any side effects.
"""
# Pure function
def add(a, b):
    return a + b

result = add(3, 5)  # Output: 8

"""
The function add() always returns the sum of its arguments a and b.
It does not modify any variables outside its scope or depend on any external state.
It produces the same result (8 in this case) for the same inputs (3 and 5).
"""




# Non-pure function example
total = 0

def add_to_total(num):
    global total
    total += num
    return total

print(add_to_total(5))  # Output: 5
print(add_to_total(3))  # Output: 8

"""
The function add_to_total() modifies the global variable total each time it is called.
It produces different results (5 and 8 respectively) depending on previous calls and the current input.
It has side effects because it modifies external state (total) outside its scope.
"""


"""
Benefits of Pure Functions:
Predictability: Easier to reason about and debug since they have no side effects.
Testability: Facilitates unit testing as they do not rely on external factors or produce unpredictable results.
Concurrency: Safe to run in parallel threads or processes without causing race conditions.
"""


"""
Pure functions are a fundamental concept in functional programming and can contribute significantly to writing cleaner,
more maintainable code in Python. By adhering to the principles of immutability and avoiding side effects, 
pure functions help ensure program reliability and ease of understanding.
"""