import pandas as pd
df = pd.read_csv('E:/Data_Science/Pandas/Project/bestsellers.csv')
print(df.head())
print(df.shape)
print(df.columns)
print(df.describe())

# Data Cleaning
df.drop_duplicates(inplace=True)

# Renaming Columns for Clarity
df.rename(columns={"Name": "Title", "Year": "Publication Year", "User Rating": "Rating"}, inplace=True)

# Converting Data Types
df["Price"] = df["Price"].astype(float)

# Analyzing Author Popularity
author_counts= df["Author"].value_counts()
print(author_counts)

# Average Rating by Genre
avg_rating_by_genre = df.groupby("Genre")["Rating"].mean()
print(avg_rating_by_genre)

# Exporting the results
# Exporting top selling authors to a CSV file
author_counts.head(10).to_csv("top_authors.csv")

# Export average rating by genre to a CSV file
avg_rating_by_genre.to_csv("avg_rating_by_genre.csv")