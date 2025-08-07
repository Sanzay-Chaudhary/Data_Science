import pandas as pd

# 1. Creating a Pandas DataFrame from scratch
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
}
df = pd.DataFrame(data, index=['a', 'b', 'c', 'd'])
print("DataFrame created from dictionary:")
print(df.loc['b':'d'])  # Slicing rows from 'b' to 'd'
