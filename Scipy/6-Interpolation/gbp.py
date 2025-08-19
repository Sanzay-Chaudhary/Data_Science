# Generating between points like between 1 and 2 there is 1.1, 1.2 etc
import numpy as np
from scipy.interpolate import interp1d
xs = np.arange(10)
ys = 2*xs + 1

interp_func = interp1d(xs, ys)
newarr = interp_func(np.arange(2.1, 3, 0.1))
print(newarr)