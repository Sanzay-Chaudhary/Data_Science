import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# mean_iq = 100
# std_iq = 15

# Generate 1000 IQ scores
iq_scores = np.random.normal(loc=100, scale=15, size=1000)

# Print basic stats
print(f"Mean IQ: {np.mean(iq_scores):.2f}")
print(f"Standard Deviation: {np.std(iq_scores):.2f}")
print(f"Minimum IQ: {np.min(iq_scores):.2f}")
print(f"Maximum IQ: {np.max(iq_scores):.2f}")

# Optional: Print first 10 simulated IQ scores
print("First 10 simulated IQ scores:", iq_scores[:10])

# Plot
sns.displot(iq_scores, bins=30, kde=True, color='skyblue')
plt.title('Simulated IQ Scores (Normal Distribution)')
plt.xlabel('IQ Score')
plt.ylabel('Frequency / Density')
plt.show()



















































