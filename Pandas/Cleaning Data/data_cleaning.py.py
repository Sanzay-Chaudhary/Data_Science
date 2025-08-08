import pandas as pd
df=pd.read_csv('E:/Data_Science/Pandas/Cleaning Data/prog3.csv')



# 1. Handling Date and NaN values
df['Date']= pd.to_datetime(df['Date'], format='mixed')  # Convert 'Date' column to datetime
df.dropna(subset=['Date'], inplace=True) # Remove rows where 'Date' is NaT



# 2. Fill NaN values in 'Calories' column with a specific value
df.fillna({"Calories": 130}, inplace=True)  # Fill NaN values in 'Calories' with 130})

# 3. Remove duplicate rows
print(df.duplicated())  # Return true for duplicate rows
df.drop_duplicates(inplace=True) # Remove duplicate rows


# 4. Cleanning wrong data
for x in df.index:
    if df.loc[x, 'Duration'] > 60:
        df.loc[x, 'Duration'] = 160

print(df)  