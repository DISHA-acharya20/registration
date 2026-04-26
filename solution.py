import numpy as np

# Define the arrays
arr1 = np.array([25, 56, 12, 85, 34, 75])
arr2 = np.array([42, 3, 86, 32, 856, 46])

# 1. Create a new NumPy array Narr with the shape equal to arr1 filled with random values
Narr = np.random.rand(*arr1.shape)
print("Narr (random values with shape of arr1):", Narr)

# 2. Permanently change the dtype of arr1 to complex
arr1 = arr1.astype(complex)
print("arr1 after changing dtype to complex:", arr1)
print("arr1 dtype:", arr1.dtype)

# 3. Transform arrays arr1 and arr2 into two matrices (arr1_mat and arr2_mat) of shape (2,3)
arr1_mat = arr1.reshape(2, 3)
arr2_mat = arr2.reshape(2, 3)
print("arr1_mat (shape 2x3):", arr1_mat)
print("arr2_mat (shape 2x3):", arr2_mat)

# Assuming the equation is element-wise multiplication (since image not visible, adjust as needed)
solution = arr1_mat * arr2_mat
print("Solution (arr1_mat * arr2_mat):", solution)