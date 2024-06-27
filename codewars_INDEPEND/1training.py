# Creating an array with 10 different types of data
data_array = [
    10,                         # Integer
    3.14,                       # Float
    "Hello, world!",            # String
    True,                       # Boolean
    [1, 2, 3],                  # List
    (4, 5, 6),                  # Tuple
    {'a': 1, 'b': 2},           # Dictionary
    {7, 8, 9},                  # Set
    None,                       # NoneType
    complex(2, 3)               # Complex number
]

# Modifying 5 elements in the array
data_array[0] = 42                        # Integer
data_array[1] = 2.718                     # Float
data_array[2] = "Goodbye, world!"         # String
data_array[3] = False                     # Boolean
data_array[4] = [4, 5, 6]                 # List

# Changing the type of 5 elements in the array
data_array[0] = str(data_array[0])               # Integer to String
data_array[1] = int(data_array[1])               # Float to Integer
data_array[2] = len(data_array[2])               # String to Integer (length of string)
data_array[3] = int(data_array[3])               # Boolean to Integer
data_array[4] = tuple(data_array[4])             # List to Tuple

# Printing the modified array with type changes
print(data_array)