import numpy as np

arr = np.arange(1,13)

print(arr)

# Q1: Convert into 3 × 4
arr_2d = arr.reshape(3,4)
print("2D array(convert into 3 X 4)")
print(arr_2d)

# Q2: Convert into 2 × 6
arr_2d = arr.reshape(2,6)
print("Convert into 2 × 6")
print(arr_2d)

# Q3: Convert into 4 × 3
arr_2d = arr.reshape(4,3)
print("Convert into 4 × 3")
print(arr_2d)

# Q4: Find Shape
print("Find Shape")
print(arr_2d.shape)

# Q5: Find Dimensions
print("Find Dimensions")
print(arr_2d.ndim)

arr = np.arange(1, 13).reshape(3, 4)
print("++++++++++++  new dataset  ++++++++++++")
print(arr)

# Q1: Convert 2D array into 1D using flatten()
flatten_arr = arr.flatten()
print("Flatten array")
print(flatten_arr)
# Q2: Check the shape after flatten
print(flatten_arr.shape)

# Q3: Convert 2D array into 1D using ravel()
ravel_arr = arr.ravel()
print("Ravel array")
print(ravel_arr)
# Q4: Check the shape after ravel
print(ravel_arr.shape)

# Q5: Difference Between flatten() and ravel()
flatten_arr = arr.flatten()
flatten_arr[0] = 100

print("Original Array:")
print(arr)

print("\nFlatten Array:")
print(flatten_arr)

ravel_arr = arr.ravel()
ravel_arr[0] = 100

print("Original Array:")
print(arr)

print("\nRavel Array:")
print(ravel_arr)

# Q-6: Create a 4 × 2 array and transpose it.
arr_4x2 = np.arange(1, 9).reshape(4, 2)
print("Original 4x2 Array:")
print(arr_4x2)
print("Dimensions:")
print(arr_4x2.ndim)
print("Size:")
print(arr_4x2.size)

transposed_arr = arr_4x2.T
print("Transposed Array:")
print(transposed_arr)
print("Dimensions:")
print(transposed_arr.ndim)
print("Size:")
print(transposed_arr.size)
