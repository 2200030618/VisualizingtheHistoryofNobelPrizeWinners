import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Load the dataset
file_path = r"C:\ODD SEM\Analysis_of_nobelprize_winners\data\nobel.csv"
nobel_df = pd.read_csv(file_path)

# Data Cleaning
# Convert 'birth_date' and 'death_date' to datetime
nobel_df["birth_date"] = pd.to_datetime(nobel_df["birth_date"], errors="coerce")
nobel_df["death_date"] = pd.to_datetime(nobel_df["death_date"], errors="coerce")

# Fill missing values in categorical columns with "Unknown"
categorical_cols = ["birth_city", "birth_country", "sex", "organization_name", "organization_city",
                    "organization_country"]
nobel_df[categorical_cols] = nobel_df[categorical_cols].fillna("Unknown")

# Visualizing the Number of Nobel Prizes Per Year
plt.figure(figsize=(12, 5))
sns.histplot(nobel_df["year"], bins=120, kde=True, color="blue")
plt.xlabel("Year")
plt.ylabel("Number of Prizes Awarded")
plt.title("Number of Nobel Prizes Awarded Per Year")
plt.show()

# Distribution of Nobel Prizes by Category
plt.figure(figsize=(10, 5))
sns.countplot(data=nobel_df, y="category", palette="magma", order=nobel_df["category"].value_counts().index)
plt.xlabel("Number of Prizes Awarded")
plt.ylabel("Category")
plt.title("Distribution of Nobel Prizes by Category")
plt.show()

# Gender Distribution Among Nobel Laureates
plt.figure(figsize=(6, 4))
sns.countplot(data=nobel_df, x="sex", palette="coolwarm")
plt.xlabel("Gender")
plt.ylabel("Number of Laureates")
plt.title("Gender Distribution of Nobel Laureates")
plt.show()

# Top 10 Countries with the Most Nobel Laureates
top_countries = nobel_df["birth_country"].value_counts().head(10)
plt.figure(figsize=(10, 5))
sns.barplot(x=top_countries.values, y=top_countries.index, palette="viridis")
plt.xlabel("Number of Laureates")
plt.ylabel("Country")
plt.title("Top 10 Countries with the Most Nobel Laureates")
plt.show()

# Gender Trends Over Time
gender_trends = nobel_df.groupby(["year", "sex"]).size().unstack().fillna(0)
plt.figure(figsize=(12, 6))
gender_trends.plot(kind="line", marker="o", figsize=(12, 6), cmap="coolwarm")
plt.xlabel("Year")
plt.ylabel("Number of Laureates")
plt.title("Gender Trends in Nobel Prizes Over Time")
plt.legend(title="Gender")
plt.show()
