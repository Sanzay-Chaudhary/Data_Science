import numpy as np
from scipy.sparse import csr_matrix

arr = np.array([[1, 0, 0], [0, 2, 0], [3, 0, 4]])

# Create a sparse matrix from the array
print(csr_matrix(arr))

# Output the non-zero elements of the sparse matrix
print(csr_matrix(arr).data)

# ✅ Correct: call the method
print(csr_matrix(arr).count_nonzero())

# Removing zero-entries from the matrix with the eliminate_zeros() method:
mat = csr_matrix(arr)
mat.eliminate_zeros()
print(mat)

# Eliminating duplicate entries with the sum_duplicates() method:
mat1 = csr_matrix(arr)
mat1.sum_duplicates()
print(mat1)

# Converting from csr(compressed sparse row) to csc(compressed sparse column) with the tocsc() method:
mat2 = csr_matrix(arr)
csc_mat = mat2.tocsc()
print(csc_mat)
