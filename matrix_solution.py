import numpy as np

# Create a 4x4 matrix filled with zeros
matrix = np.zeros((4, 4))

# Add values 4, 5, 6 above the main diagonal (on the super diagonal)
# Super diagonal: positions where column = row + 1
values = [4, 5, 6]

for i in range(len(values)):
    matrix[i, i+1] = values[i]

print("4x4 Matrix with values 4, 5, 6 on the super diagonal:")
print(matrix)
print("\nAs integer format:")
print(matrix.astype(int))
