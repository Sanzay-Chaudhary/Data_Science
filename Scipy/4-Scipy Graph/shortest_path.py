import numpy as np
from scipy.sparse.csgraph import connected_components
from scipy.sparse.csgraph import dijkstra
from scipy.sparse.csgraph import floyd_warshall
from scipy.sparse.csgraph import bellman_ford
from scipy.sparse import csr_matrix

arr = np.array([
  [0, 1, 2],
  [1, 0, 0],
  [2, 0, 0]
])

 # Output the number of connected components and their labels
newarr = csr_matrix(arr)
print(connected_components(newarr))

# Output the shortest path lengths and predecessors from the source node 0 through dijkstra method
newarr1 = csr_matrix(arr)
print(dijkstra(newarr1, return_predecessors=True, indices=0)) 

# Output the shortest path lengths and predecessors for all pairs of nodes through Floyd-Warshall method
newarr2 = csr_matrix(arr)
print(floyd_warshall(newarr2, return_predecessors=True)) 

# Output the shortest path lengths from node 0 to all other nodes through bellman-ford method
newarr3 = csr_matrix(arr)
print(bellman_ford(newarr3, return_predecessors=True, indices=0))