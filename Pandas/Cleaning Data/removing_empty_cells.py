import pandas as pd
df=pd.read_csv('E:/Data_Science/Pandas/Cleaning Data/prog3.csv')

df.dropna(inplace=True)  # Drop rows with any NaN values
print(df.to_string)  