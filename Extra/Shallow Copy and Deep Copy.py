"""
"deep copy" and "shallow copy" are techniques used to create copies of objects, especially for mutable objects
like lists and dictionaries, where you might need to manipulate data without affecting the original object. These
concepts are important because they determine how nested objects and references are handled during the copying
process.
"""


"""
Shallow Copy: Copies the top-level structure of a mutable object. 
Nested objects are not copied; instead, references to them are copied. 
Changes to nested objects in the original affect the shallow copy, and vice versa
"""

import copy

# Creating a list with nested lists
list1 = [[1, 2], [3, 4]]
shallow_copy = copy.copy(list1)

# Modify the nested list in the original
list1[0][0] = 0

print(list1)         # Output: [[0, 2], [3, 4]]
print(shallow_copy)  # Output: [[0, 2], [3, 4]]



"""
Deep Copy: Creates a fully independent copy of the original object and all its nested objects.
Changes to the original or its nested objects do not affect the deep copy, and vice versa.
"""

import copy

# Creating a list with nested lists
list1 = [[1, 2], [3, 4]]
deep_copy = copy.deepcopy(list1)

# Modify the nested list in the original
list1[0][0] = 0

print(list1)      # Output: [[0, 2], [3, 4]]
print(deep_copy)  # Output: [[1, 2], [3, 4]]



"""

Key Difference:

Shallow copy creates a new object but doesn't recursively copy nested objects.
Deep copy creates a new object and recursively copies all nested objects.
When to Use:

Use shallow copy when you want to clone an object and you're okay with changes to nested objects affecting both the original and the copy.
Use deep copy when you need a completely independent copy of the original object and all its contents.

"""