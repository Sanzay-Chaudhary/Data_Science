import pandas as pd
df = pd.read_json('E:/Data_Science/Pandas/Read JSON/prog2.json')
print("DataFrame created from json file:")
print(df) # Print the entire DataFrame with the middle rows replaced by dots (if large)
print(df.head())  # Display first 5 rows
print(df.head(10))  # Display first 10 rows
print(df.tail())  # Display last 5 rows
print(df.tail(10))  # Display last 10 rows
# print(df[['Duration', 'Pulse']].head())  # Display first 5 rows of 'Name' and 'Age' columns

print(df.info())  # Display DataFrame information
print(df.to_string())  # Print the entire DataFrame as a string