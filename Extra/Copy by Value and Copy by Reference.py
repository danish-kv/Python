"""
In Python, understanding "copy by value" and "copy by reference" involves how objects are passed and manipulated in memory.
"""

"""
Copy by Value :-
In Python, variables of immutable types (like integers, strings, and tuples) are passed by value. 
When you assign a variable to another variable or pass it to a function, a copy of the object's value is made. 
Modifications to one variable do not affect the other.
"""

# Copying by value (immutable type: integer)
x = 10
y = x  # y is a copy of the value of x
x = 20  # Modifying x does not affect y

print(x)  # Output: 20
print(y)  # Output: 10



"""
Copy by Reference
In Python, variables of mutable types (like lists, dictionaries, and sets) are passed by reference. 
When you assign a variable to another variable or pass it to a function, you are actually passing a reference (or pointer) to the object in memory. 
Modifications to the object through one variable affect all references to that object.
"""

# Copying by reference (mutable type: list)
list1 = [1, 2, 3]
list2 = list1  # list2 is a reference to the same list object as list1
list1.append(4)  # Modifying list1 also modifies list2

print(list1)  # Output: [1, 2, 3, 4]
print(list2)  # Output: [1, 2, 3, 4]
