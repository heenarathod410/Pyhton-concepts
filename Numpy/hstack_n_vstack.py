import numpy as np

A = np.array([
    [1, 2],
    [3, 4]
])

B = np.array([
    [5, 6],
    [7, 8]
])

print("Array A")
print(A)

print("\nArray B")
print(B)

# Q1: Horizontally Stack Two 2D Arrays
hstacked_arr = np.hstack((A, B))
print("\nHorizontally Stacked Array:")
print(hstacked_arr)

# Q2: vertically Stack Two 2D Arrays
vstacked_arr = np.vstack((A, B))
print("\nVertically Stacked Array:")
print(vstacked_arr)

# Q3: compare with concatenate() function
concatenated_arr = np.concatenate((A, B), axis=1)
print("\nConcatenated Array (axis=1):")
print(concatenated_arr)
print("\nnp.hstack((A, B)):")
print(np.hstack((A, B)))
print("hstacked_arr is equal to concatenated_arr:", np.array_equal(hstacked_arr, concatenated_arr))

print("\nConcatenated Array (axis=0):")
concatenated_arr_axis0 = np.concatenate((A, B), axis=0)
print(concatenated_arr_axis0)
print("\nnp.vstack((A, B)):")
print(np.vstack((A, B)))
print("vstacked_arr is equal to concatenated_arr_axis0:", np.array_equal(vstacked_arr, concatenated_arr_axis0))

# Q4: Stack 3 Arrays
c = np.array([
    [9, 10],
    [11, 12]
])

hstacked_3d = np.hstack((A, B, c))
print("\nHorizontally Stacked Array (3 Arrays):")
print(hstacked_3d)
print("\nShape of Horizontally Stacked Array (3 Arrays):")
print(hstacked_3d.shape)

vstacked_3d = np.vstack((A, B, c))
print("\nVertically Stacked Array (3 Arrays):") 
print(vstacked_3d)
print("\nShape of Vertically Stacked Array (3 Arrays):")
print(vstacked_3d.shape)

# Q5: What Happens with Different Shapes?
D = np.array([
    [1, 2, 3]
])

print(D.shape)

print("\nAttempting to horizontally stack A and D:")
try:
    hstacked_diff_shape = np.hstack((A, D))
    print(hstacked_diff_shape)
except ValueError as e:
    print("Error:", e)

print("\nAttempting to vertically stack A and D:")
try:
    vstacked_diff_shape = np.vstack((A, D))
    print(vstacked_diff_shape)
except ValueError as e:
    print("Error:", e)