# UNPACKING OPERATOR
# The unpacking operator is used to unpack the elements of a list or a tuple into individual variables. It is denoted by the asterisk (*) symbol.
# Example 1: Unpacking a list
print("Example 1: Unpacking a list")
my_list = [1, 2, 3]
a, b, c = my_list
print(a)  # Output: 1
print(b)  # Output: 2
print(c)  # Output: 3

# Example 2: Unpacking a tuple
print("Example 2: Unpacking a tuple")
my_tuple = (4, 5, 6)
x, y, z = my_tuple
print(x)  # Output: 4
print(y)  # Output: 5
print(z)  # Output: 6

# Example 3: Unpacking with the unpacking operator
print("Example 3: Unpacking with the unpacking operator")
my_list = [1, 2, 3, 4, 5]
a, *b, c = my_list
print(a)  # Output: 1
print(b)  # Output: [2, 3, 4]
print(c)  # Output: 5

# Example 4: Unpacking with the unpacking operator in a function
print("Example 4: Unpacking with the unpacking operator in a function")
def my_function(a, b, c):
    print(a)
    print(b)
    print(c)
my_list = [1, 2, 3]
my_function(*my_list)  # Output: 1, 2, 3

# Example 5: Unpacking with the unpacking operator in a function with variable number of arguments
print("Example 5: Unpacking with the unpacking operator in a function with variable number of arguments")
def my_function(*args):
    for arg in args:
        print(arg)
my_list = [1, 2, 3, 4, 5]
my_function(*my_list)  # Output: 1, 2, 3, 4, 5

# Example 6: Unpacking with the unpacking operator in a function with keyword arguments
print("Example 6: Unpacking with the unpacking operator in a function with keyword arguments")
def my_function(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
my_dict = {'a': 1, 'b': 2, 'c': 3}
my_function(**my_dict)  # Output: a: 1, b: 2, c: 3

# Example 7: Unpacking with the unpacking operator in a function with variable number of keyword arguments
print("Example 7: Unpacking with the unpacking operator in a function with variable number of keyword arguments")
def my_function(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
my_function(**my_dict)  # Output: a: 1, b: 2, c: 3, d: 4, e: 5

# Example 8: Unpacking with the unpacking operator in a function with both variable number of arguments and keyword arguments
print("Example 8: Unpacking with the unpacking operator in a function with both variable number of arguments and keyword arguments")
def my_function(*args, **kwargs):
    for arg in args:
        print(arg)
    for key, value in kwargs.items():
        print(f"{key}: {value}")
my_list = [1, 2, 3]
my_dict = {'a': 4, 'b': 5, 'c': 6}
my_function(*my_list, **my_dict)  # Output: 1, 2, 3, a: 4, b: 5, c: 6

# Example 9: Unpacking with the unpacking operator in a function with default arguments
print("Example 9: Unpacking with the unpacking operator in a function with default arguments")
def my_function(a, b, c=0):
    print(a)
    print(b)
    print(c)
my_list = [1, 2]
my_function(*my_list)  # Output: 1, 2, 0

# Example 10: Unpacking with the unpacking operator in a function with default arguments and variable number of arguments
print("Example 10: Unpacking with the unpacking operator in a function with default arguments and variable number of arguments")
def my_function(a, b, c=0, *args):
    print(a)
    print(b)
    print(c)
    for arg in args:
        print(arg)
my_list = [1, 2, 3, 4, 5]
my_function(*my_list)  # Output: 1, 2, 3, 4, 5

# Example 11: Unpacking with the unpacking operator in a function with default arguments and variable number of keyword arguments
print("Example 11: Unpacking with the unpacking operator in a function with default arguments and variable number of keyword arguments")
def my_function(a, b, c=0, **kwargs):
    print(a)
    print(b)
    print(c)
    for key, value in kwargs.items():
        print(f"{key}: {value}")
my_list = [1, 2]
my_dict = {'d': 4, 'e': 5, 'f': 6}
my_function(*my_list, **my_dict)  # Output: 1, 2, 0, d: 4, e: 5, f: 6

# Example 12: Unpacking with the unpacking operator in a function with default arguments, variable number of arguments, and variable number of keyword arguments
print("Example 12: Unpacking with the unpacking operator in a function with default arguments, variable number of arguments, and variable number of keyword arguments")
def my_function(a, b, c=0, *args, **kwargs):
    print(a)
    print(b)
    print(c)
    for arg in args:
        print(arg)
    for key, value in kwargs.items():
        print(f"{key}: {value}")
my_list = [1, 2, 3, 4, 5]
my_dict = {'d': 6, 'e': 7, 'f': 8}
my_function(*my_list, **my_dict)  # Output: 1, 2, 3, 4, 5, d: 6, e: 7, f: 8

# Example 13: Unpacking with the unpacking operator in a function with default arguments, variable number of arguments, variable number of keyword arguments, and keyword-only arguments
def my_function(a, b, c=0, *args, d=0, e=0, f=0, **kwargs):
    print(a)
    print(b)
    print(c)
    for arg in args:
        print(arg)
    print(d)
    print(e)
    print(f)
    for key, value in kwargs.items():
        print(f"{key}: {value}")
my_list = [1, 2, 3, 4, 5]
my_dict = {'d': 6, 'e': 7, 'f': 8, 'g': 9, 'h': 10, 'i': 11}
my_function(*my_list, **my_dict)  # Output: 1, 2, 3, 4, 5, 6, 7, 8, g: 9, h: 10, i: 11

# Example 14: Unpacking with the unpacking operator in a function with default arguments, variable number of arguments, variable number of keyword arguments, keyword-only arguments, and positional-only arguments
print("Example 14: Unpacking with the unpacking operator in a function with default arguments, variable number of arguments, variable number of keyword arguments, keyword-only arguments, and positional-only arguments")
def my_function(a, b, c=0, *args, d=0, e=0, f=0, **kwargs):
    print(a)
    print(b)
    print(c)
    for arg in args:
        print(arg)
    print(d)
    print(e)
    print(f)
    for key, value in kwargs.items():
        print(f"{key}: {value}")
my_list = [1, 2, 3, 4, 5]
my_dict = {'d': 6, 'e': 7, 'f': 8, 'g': 9, 'h': 10, 'i': 11}
my_function(*my_list, **my_dict)  # Output: 1, 2, 3, 4, 5, 6, 7, 8, g: 9, h: 10, i: 11

# Example 15: Unpacking with the unpacking operator in a function with default arguments, variable number of arguments, variable number of keyword arguments, keyword-only arguments, positional-only arguments, and variable number of positional-only arguments
print("Example 15: Unpacking with the unpacking operator in a function with default arguments, variable number of arguments, variable number of keyword arguments, keyword-only arguments, positional-only arguments, and variable number of positional-only arguments") 
def my_function(a, b, c=0, *args, d=0, e=0, f=0, **kwargs):
    print(a)
    print(b)
    print(c)
    for arg in args:
        print(arg)
    print(d)
    print(e)
    print(f)
    for key, value in kwargs.items():
        print(f"{key}: {value}")
my_list = [1, 2, 3, 4, 5]
my_dict = {'d': 6, 'e': 7, 'f': 8, 'g': 9, 'h': 10, 'i': 11}
my_function(*my_list, **my_dict)  # Output: 1, 2, 3, 4, 5, 6, 7, 8, g: 9, h: 10, i: 11

# Example 16: Unpacking with the unpacking operator in a function with default arguments, variable number of arguments, variable number of keyword arguments, keyword-only arguments, positional-only arguments, variable number of positional-only arguments, and variable number of keyword-only arguments
print("Example 16: Unpacking with the unpacking operator in a function with default arguments, variable number of arguments, variable number of keyword arguments, keyword-only arguments, positional-only arguments, variable number of positional-only arguments, and variable number of keyword-only arguments")
def my_function(a, b, c=0, *args, d=0, e=0, f=0, **kwargs):
    print(a)
    print(b)
    print(c)
    for arg in args:
        print(arg)
    print(d)
    print(e)
    print(f)
    for key, value in kwargs.items():
        print(f"{key}: {value}")
my_list = [1, 2, 3, 4, 5]
my_dict = {'d': 6, 'e': 7, 'f': 8, 'g': 9, 'h': 10, 'i': 11, 'j': 12, 'k': 13, 'l': 14}
my_function(*my_list, **my_dict)  # Output: 1, 2, 3, 4, 5, 6, 7, 8, g: 9, h: 10, i: 11, j: 12, k: 13, l: 14

# Merging lists
print("Merging lists")
list1 = [1, 2, 3]
list2 = [4, 5, 6]
merged_list = [*list1, *list2]
print(merged_list)  # Output: [1, 2, 3, 4, 5, 6]

# Merging dictionaries
print("Merging dictionaries")
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'d': 4, 'e': 5, 'f': 6}
merged_dict = {**dict1, **dict2}
print(merged_dict)  # Output: {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}

# Merging sets
print("Merging sets")
set1 = {1, 2, 3}
set2 = {4, 5, 6}
merged_set = {*set1, *set2}
print(merged_set)  # Output: {1, 2, 3, 4, 5, 6}

# Merging tuples
print("Merging tuples")
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
merged_tuple = (*tuple1, *tuple2)
print(merged_tuple)  # Output: (1, 2, 3, 4, 5, 6)

# Merging strings
string1 = "Hello"
string2 = "World"
merged_string = f"{string1} {string2}"  
print(merged_string)  # Output: "Hello World"

# Merging lists with unpacking operator and additional elements
list1 = [1, 2, 3]
list2 = [4, 5, 6]
merged_list = [0, *list1, *list2, 7]
print(merged_list)  # Output: [0, 1, 2, 3, 4, 5, 6, 7]

# Merging dictionaries with unpacking operator and additional key-value pairs
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'d': 4, 'e': 5, 'f': 6}
merged_dict = {**dict1, **dict2, 'g': 7, 'h': 8, 'i': 9}
print(merged_dict)  # Output: {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9}

# Merging sets with unpacking operator and additional elements
set1 = {1, 2, 3}
set2 = {4, 5, 6}
merged_set = {0, *set1, *set2, 7}
print(merged_set)  # Output: {0, 1, 2, 3, 4, 5, 6, 7}

# Merging tuples with unpacking operator and additional elements
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
merged_tuple = (0, *tuple1, *tuple2, 7)
print(merged_tuple)  # Output: (0, 1, 2, 3, 4, 5, 6, 7)

# Merging strings with unpacking operator and additional elements
string1 = "Hello"
string2 = "World"
merged_string = f"{string1} {string2}!"
print(merged_string)  # Output: "Hello World!"

# Unpacking with the unpacking operator in a function with default arguments, variable number of arguments, variable number of keyword arguments, keyword-only arguments, positional-only arguments, variable number of positional-only arguments, variable number of keyword-only arguments, and keyword-only variable number of keyword arguments
def my_function(a, b, c=0, *args, d=0, e=0, f=0, **kwargs):
    print(a)
    print(b)
    print(c)
    for arg in args:
        print(arg)
    print(d)
    print(e)
    print(f)
    for key, value in kwargs.items():
        print(f"{key}: {value}")
my_list = [1, 2, 3, 4, 5]
my_dict = {'d': 6, 'e': 7, 'f': 8, 'g': 9, 'h': 10, 'i': 11, 'j': 12, 'k': 13, 'l': 14, 'm': 15, 'n': 16, 'o': 17}
my_function(*my_list, **my_dict)  # Output: 1, 2, 3, 4, 5, 6, 7, 8, g: 9, h: 10, i: 11, j: 12, k: 13, l: 14, m: 15, n: 16, o: 17

