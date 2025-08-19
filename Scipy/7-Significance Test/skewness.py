import numpy as np
from scipy.stats import skew, kurtosis, describe   
v = np.random.normal(size=100)
print("Skewness:", skew(v))
print("Kurtosis:", kurtosis(v))
print("Descriptive statistics:", describe(v))
# --- IGNORE ---



