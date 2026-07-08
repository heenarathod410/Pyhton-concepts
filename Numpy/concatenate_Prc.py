import numpy as np

# 📚 Topic: concatenate()
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

print("Array 1:")
print(arr1)

print("\nArray 2:")
print(arr2)

# Q-1: Concatenate 1D arrays
concatenated_arr = np.concatenate((arr1, arr2))
print("Concatenated Array:")
print(concatenated_arr)

# Q-2: Find shape
print("Shape of Concatenated Array:")
print(concatenated_arr.shape)

# Q3: Concatenate Two 2D Arrays Row-wise (axis=0)
arr1 = np.array([
    [1, 2],
    [3, 4]
])

arr2 = np.array([
    [5, 6],
    [7, 8]
])

print("2D Array concatenation (Row-wise):")
result = np.concatenate((arr1, arr2), axis=0)

print(result)

print("Shape of Concatenated 2D Array (Row-wise):")
print(result.shape)

# Q4: Concatenate Two 2D Arrays Column-wise (axis=1)
print("2D Array concatenation (Column-wise):")
result = np.concatenate((arr1, arr2), axis=1)
print(result)
print("Shape of Concatenated 2D Array (Column-wise):")
print(result.shape)

# Q5: Print shapes
print("Shapes of the original arrays and the result:")
print("Array 1 shape:", arr1.shape)
print(arr1.shape)
print("Array 2 shape:", arr2.shape)
print(arr2.shape)
print("Result shape:", result.shape)
print(result.shape)

# Q6
arr3 = np.array([7, 8, 9])

print("Concatenating three 1D arrays:")
result = np.concatenate((arr1.flatten(), arr2.flatten(), arr3))
print(result)

# Q7

# Create two arrays:

A = np.arange(1, 7).reshape(2, 3)

B = np.arange(7, 13).reshape(2, 3)

# Concatenate along axis 0 (row-wise)
result_axis0 = np.concatenate((A, B), axis=0)
print("Concatenation along axis 0 (row-wise):")
print(result_axis0)

# Concatenate along axis 1 (column-wise)
result_axis1 = np.concatenate((A, B), axis=1)
print("Concatenation along axis 1 (column-wise):")
print(result_axis1)

A.shape = (2, 3)
B.shape = (3, 2)

# Concatenate along axis 0 (row-wise)
result_axis0 = np.concatenate((A, B), axis=0)
print("Concatenation along axis 0 (row-wise) with different shapes:")
print(result_axis0)

# Concatenate along axis 1 (column-wise)
result_axis1 = np.concatenate((A, B), axis=1)
print("Concatenation along axis 1 (column-wise) with different shapes:")
print(result_axis1)