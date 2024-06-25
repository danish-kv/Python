"""
Pickling:-
Pickling is the process of converting a Python object into a byte stream. This byte stream can then be
stored in a file or transmitted over a network. Python provides a built-in module named pickle for this purpose.
"""

import pickle

# Define a Python object
data = {
    'name': 'Alice',
    'age': 30,
    'is_student': False,
    'scores': [85, 90, 92]
}

# Open a file in binary write mode
with open('data.pkl', 'wb') as file:
    # Use pickle.dump() to serialize the object and write it to the file
    pickle.dump(data, file)

print("Data has been pickled and saved to 'data.pkl'")




"""
Unpickling:-
Unpickling is the process of converting a byte stream (from a file or any other source) back into a 
Python object. This is the reverse process of pickling.
"""


# Open the file in binary read mode
with open('data.pkl', 'rb') as file:
    # Use pickle.load() to deserialize the byte stream to a Python object
    loaded_data = pickle.load(file)

print("Data has been unpickled from 'data.pkl'")
print(loaded_data)



"""
In short:-

Pickling: Converting a Python object to a byte stream using pickle.dump().
Unpickling: Converting a byte stream back to a Python object using pickle.load().
Use Cases: Storing objects in files, transmitting objects over networks, etc.
Security Considerations: Only unpickle data from trusted sources due to security risks.

"""
