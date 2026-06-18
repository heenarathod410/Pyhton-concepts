# List comprehension is a concise way to create lists in Python. It consists of brackets containing an expression followed by a for clause, then zero or more for or if clauses. The expressions can be anything, meaning you can put in all kinds of objects in lists.

# syntax: [expression for item in iterable if condition == True]
squares = [x**2 for x in range(10)]
print(squares)

# You can also add a condition to filter items from the iterable. For example, to create a list of squares of even numbers:
even_squares = [x**2 for x in range(10) if x % 2 == 0]
print(even_squares)

# List comprehensions can also be used with nested loops. For example, to create a list of tuples containing pairs of numbers:
pairs = [(x, y) for x in range(3) for y in range(3)]
print(pairs)

# You can also use list comprehensions to create a new list by applying a function to each item in an iterable. For example, to create a list of the lengths of words in a list:
words = ['hello', 'world', 'python', 'comprehension']
lengths = [len(word) for word in words]
print(lengths)

# dictionary comprehension is similar to list comprehension but creates a dictionary instead of a list. The syntax is {key: value for item in iterable if condition == True}. For example, to create a dictionary of squares of numbers:
# syntax: {key: value for item in iterable if condition == True}
squares_dict = {x: x**2 for x in range(10)}
print(squares_dict)

# You can also add a condition to filter items from the iterable. For example, to create a dictionary of squares of even numbers:
even_squares_dict = {x: x**2 for x in range(10) if x % 2 == 0}
print(even_squares_dict)

# Set comprehension is similar to list comprehension but creates a set instead of a list. The syntax is {expression for item in iterable if condition == True}. For example, to create a set of squares of numbers:
# syntax: {expression for item in iterable if condition == True}
unique = {x%3 for x in range(10)}
print(unique)

# You can also add a condition to filter items from the iterable. For example, to create a set of squares of even numbers:
even_unique = {x%3 for x in range(10) if x % 2 == 0}
print(even_unique)

# 💡 Real-Life Example (useful for you)
# Let's say you have a list of temperatures in Celsius and you want to convert them to Fahrenheit. You can use a list comprehension to do this in a single line of code:
celsius = [0, 10, 20, 30, 40]
fahrenheit = [(temp * 9/5) + 32 for temp in celsius]
print(fahrenheit)

# You can also use a dictionary comprehension to create a mapping of temperatures in Celsius to Fahrenheit:
temp_dict = {temp: (temp * 9/5) + 32 for temp in celsius}
print(temp_dict)

# Finally, you can use a set comprehension to create a set of unique temperatures in Fahrenheit:
unique_fahrenheit = {(temp * 9/5) + 32 for temp in celsius}
print(unique_fahrenheit)

# Convert prices list with GST
prices = [100, 200, 300, 400, 500]
gst_prices = [price * 1.18 for price in prices] # Assuming GST is 18%
print(gst_prices)
