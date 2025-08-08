import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('E:/Data_Science/Pandas/Correlation/correlation.csv')

print(df.corr()) # Display the correlation matrix
df.plot(kind='scatter', x='Duration', y='Calories') # Scatter plot between Duration and Calories
df['Duration'].plot(kind='hist') # Histogram of Duration
plt.show()