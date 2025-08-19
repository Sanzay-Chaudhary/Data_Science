
# How many people of each race are represented in this dataset? This should be a Pandas series with race names as the index labels. (race column)
# What is the average age of men?
# What is the percentage of people who have a Bachelor's degree?
# What percentage of people with advanced education (Bachelors, Masters, or Doctorate) make more than 50K?
# What percentage of people without advanced education make more than 50K?
# What is the minimum number of hours a person works per week?
# What percentage of the people who work the minimum number of hours per week have a salary of more than 50K?
# What country has the highest percentage of people that earn >50K and what is that percentage?
# Identify the most popular occupation for those who earn >50K in India.


import pandas as pd

# 1. Import the data and strip column whitespace
df = pd.read_csv('E:/Data_Science/Data Analysis/Demographic Data Analyzer/demographic_data.csv')


# =========================
# 1. Count of each race
race_count = df['race'].value_counts()

# 2. Average age of men
average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)

# 3. Percentage of people with Bachelors
percentage_bachelors = round((df['education'] == 'Bachelors').mean() * 100, 1)

# 4. Percentage with advanced education (>50K)
advanced_education = ['Bachelors', 'Masters', 'Doctorate']
adv_ed_df = df[df['education'].isin(advanced_education)]
higher_edu_rich = round((adv_ed_df['salary'] == '>50K').mean() * 100, 1)

# 5. Percentage without advanced education (>50K)
non_adv_df = df[~df['education'].isin(advanced_education)]
lower_edu_rich = round((non_adv_df['salary'] == '>50K').mean() * 100, 1)

# 6. Minimum hours per week
min_work_hours = df['hours-per-week'].min()

# 7. % of people who work minimum hours with >50K
num_min_workers = df[df['hours-per-week'] == min_work_hours]
rich_min_workers = round((num_min_workers['salary'] == '>50K').mean() * 100, 1)

# 8. Country with highest % earning >50K
country_salary = df.groupby('native-country')['salary'].apply(lambda x: (x=='>50K').mean())
highest_earning_country = country_salary.idxmax()
highest_earning_country_percentage = round(country_salary.max() * 100, 1)

# 9. Most popular occupation in India for >50K
india_rich = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]
top_IN_occupation = india_rich['occupation'].value_counts().idxmax()

# =========================
# Print results
if __name__ == "__main__":
    print("Number of each race:\n", race_count)
    print("Average age of men:", average_age_men)
    print("Percentage with Bachelors:", percentage_bachelors)
    print("% with advanced education earning >50K:", higher_edu_rich)
    print("% without advanced education earning >50K:", lower_edu_rich)
    print("Minimum hours per week:", min_work_hours)
    print("% of people working min hours earning >50K:", rich_min_workers)
    print("Country with highest % earning >50K:", highest_earning_country)
    print("Highest % in that country:", highest_earning_country_percentage)
    print("Top occupation in India for >50K:", top_IN_occupation)
