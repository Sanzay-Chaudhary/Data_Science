import numpy as np
from scipy.stats import skew, kurtosis, describe   
v = np.random.normal(size=100)

# positive skew indicates a longer tail on the right and negative skew indicates a longer tail on the left
print("Skewness:", skew(v))  

# positive kustosis means a heavy tail and negative kurtosis means a light tail
print("Kurtosis:", kurtosis(v))


# summary statistics
print("Descriptive statistics:", describe(v))
# --- IGNORE ---



