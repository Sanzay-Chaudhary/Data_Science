# Which carton should you get?

import numpy as np
egg_carton1 = np.array([
  [0.89, 0.90, 0.83, 0.89, 0.97, 0.98], 
  [0.95, 0.95, 0.89, 0.95, 0.23, 0.99]
])

egg_carton2 = np.array([
  [0.89, 0.95, 0.84, 0.92, 0.94, 0.93], 
  [0.93, 0.95, 0.02, 0.03, 0.23, 0.99]
])

egg_carton3 = np.array([
  [0.83, 0.95, 0.89, 0.54, 0.37, 0.92], 
  [0.98, 0.99, 0.19, 0.23, 0.89, 0.91]
])

avg_egg_carton1 = np.average(egg_carton1)
avg_egg_cartoon2 = np.average(egg_carton2)
avg_egg_carton3 = np.average(egg_carton3)
print("Average of egg carton 1:", avg_egg_carton1)
print("Average of egg carton 2:", avg_egg_cartoon2)
print("Average of egg carton 3:", avg_egg_carton3)
