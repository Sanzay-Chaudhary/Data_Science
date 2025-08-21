import pandas as pd

df = pd.read_csv('E:/Data_Science/Data Analysis/YT Plot/most_subscribed_youtube_channels.csv')

# Convert 'subscribers' column to numeric (remove commas first)
df['subscribers'] = df['subscribers'].str.replace(',', '').astype(float)
print(df)


import matplotlib.pyplot as plt


# Section 1: Make a Histogram
plt.hist(df['subscribers'], bins=30, edgecolor='black')
plt.xlabel('subscribers')
plt.title('subscribers count')
plt.show()


# Section 2: Make a Pie Chart
category_subs = df.groupby('category')['subscribers'].sum()
plt.pie(category_subs, labels=category_subs.index, autopct='%1.1f%%')
plt.title('Subscribers by Category')
plt.show()


# Section 3: Make a Box Plot
plt.boxplot(df['started'], patch_artist=True, notch=True, vert=False,)
plt.ylabel('started')
plt.title('Years Started')
plt.show()