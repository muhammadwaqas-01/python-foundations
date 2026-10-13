import numpy as np

x = np.arange(12)
print("Array:", x)
print("Shape:", x.shape)

# x.reshape(3, 4)  # This will return a new array with shape (3, 4)
print("Reshaped Array:\n", x.reshape(3, 4))
# Prediction: The new shape will be (3, 4) because we are reshaping the 1D array of 12 elements into a 2D array with 3 rows and 4 columns.
print("New Shape:", x.reshape(3, 4).shape)

# x.reshape(4,3)  # This will return a new array with shape (4, 3)
print("Reshaped Array:\n", x.reshape(4, 3))
# Prediction: The new shape will be (4, 3) because we are reshaping the 1D array of 12 elements into a 2D array with 4 rows and 3 columns.
print("New Shape:", x.reshape(4, 3).shape)

# x.reshape(2, 6)  # This will return a new array with shape (2, 6)
print("Reshaped Array:\n", x.reshape(2, 6))
# Prediction: The new shape will be (2, 6) because we are reshaping the 1D array of 12 elements into a 2D array with 2 rows and 6 columns.
print("New Shape:", x.reshape(2, 6).shape)


#x.reshape(2,2,3)  # This will return a new array with shape (2, 2, 3)
print("Reshaped Array:\n", x.reshape(3, 2, 2))
# Prediction: The new shape will be (3, 2, 2) because we are reshaping the 1D array of 12 elements into a 3D array with 3 blocks, each containing 2 rows and 2 columns.
print("New Shape:", x.reshape(3, 2, 2).shape)

#x.reshape(4,-1)  # This will return a new array with shape (4, 3)
print("Reshaped Array:\n", x.reshape(4, -1))
# Prediction: The new shape will be (4, 3) because we are reshaping the 1D array of 12 elements into a 2D array with 4 rows and an automatically calculated number of columns (-1 indicates that NumPy should infer the size of that dimension).
print("New Shape:", x.reshape(4, -1).shape)

#x.reshape(5,3)  # This will raise an error because the total number of elements does not match
try:
    print("Reshaped Array:\n", x.reshape(5, 3))
except ValueError as e:
    print("Error:", e)

#matrix = np.arange(12).reshape(3, 4)
matrix = x.reshape(3, 4)
print("Original Matrix:\n", x.reshape(3, 4))
print("Original Shape:", x.reshape(3, 4).shape)

# Transpose the matrix
transposed_matrix = x.reshape(3, 4).T
print("Transposed Matrix:\n", transposed_matrix)
print("Transposed Shape:", transposed_matrix.shape)

# Ravel the matrix to a 1D array
raveled_array = x.reshape(3, 4).T.ravel()
print("Raveled Array:", raveled_array)
print("Raveled Shape:", raveled_array.shape)

raveled_array = matrix.ravel()
print("Raveled matrix Array:", raveled_array)
print("Raveled matrix Shape:", raveled_array.shape)

# -1 in reshape allows NumPy to automatically calculate the appropriate dimension based on the other specified dimensions. For example, if you specify one dimension and use -1 for the other, NumPy will infer the size of that dimension to ensure the total number of elements remains consistent.
# x.reshape(5,3)  # This will raise an error because the total number of elements does not match