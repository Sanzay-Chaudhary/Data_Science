import numpy as np
from scipy.sparse.csgraph import breadth_first_order
from scipy.sparse.csgraph import depth_first_order
from scipy.sparse import csr_matrix

arr = np.array([
  [0, 1, 0, 1],
  [1, 1, 1, 1],
  [2, 1, 1, 0],
  [0, 1, 0, 1]
])

# Output the breadth-first order of the graph starting from node 1
arr1 = csr_matrix(arr)
print(breadth_first_order(arr1, 1))

# Output the depth-first order of the graph starting from node 1
arr2 = csr_matrix(arr)
print(depth_first_order(arr2, 1))
