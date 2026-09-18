import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# --------------------------------------------------
# 1. LOAD DATASET
# --------------------------------------------------

df = pd.read_csv("W1D3_indian_sales_cleaned.csv")

print("=" * 50)
print("W1D4 - EXPLORATORY DATA ANALYSIS")
print("=" * 50)


# --------------------------------------------------
# 2. DATASET INFORMATION
# --------------------------------------------------

print("\n1. DATASET SHAPE")
print("----------------")
print(df.shape)


print("\n2. DATASET INFO")
print("---------------")
df.info()


print("\n3. DESCRIPTIVE STATISTICS")
print("-------------------------")
print(df.describe())


print("\n4. MISSING VALUES")
print("-----------------")
print(df.isnull().sum())


# --------------------------------------------------
# 3. FIVE OBSERVATIONS
# --------------------------------------------------

print("\n5 OBSERVATIONS")
print("--------------")

print(
    f"1. The dataset contains {df.shape[0]} rows "
    f"and {df.shape[1]} columns."
)

print(
    f"2. Sales values range from {df['sales'].min():.2f} "
    f"to {df['sales'].max():.2f}."
)

print(
    f"3. The average sales value is "
    f"{df['sales'].mean():.2f}."
)

print(
    f"4. The most common city is "
    f"{df['city'].value_counts().idxmax()}."
)

print(
    f"5. There are {df.isnull().sum().sum()} missing values "
    f"after data cleaning."
)


# --------------------------------------------------
# 4. DISTRIBUTION OF NUMERIC COLUMNS
# --------------------------------------------------

numeric_columns = df.select_dtypes(include="number").columns

for column in numeric_columns:

    plt.figure(figsize=(8, 5))

    plt.hist(df[column], bins=10)

    plt.title(f"Distribution of {column}")
    plt.xlabel(column)
    plt.ylabel("Frequency")

    plt.tight_layout()

    # Save the distribution plot
    plt.savefig(f"W1D4_distribution_{column}.png")

    plt.show()


# --------------------------------------------------
# 5. CORRELATION HEATMAP
# --------------------------------------------------

correlation = df[numeric_columns].corr()

plt.figure(figsize=(8, 6))

sns.heatmap(
    correlation,
    annot=True,
    cmap="coolwarm",
    fmt=".2f"
)

plt.title("Correlation Heatmap")

plt.tight_layout()

plt.savefig("W1D4_correlation_heatmap.png")

plt.show()


# --------------------------------------------------
# 6. TOP-10 CATEGORY COUNTS
# --------------------------------------------------

categorical_columns = df.select_dtypes(
    include=["object", "string"]
).columns

for column in categorical_columns:

    top_categories = df[column].value_counts().head(10)

    plt.figure(figsize=(8, 5))

    top_categories.plot(kind="bar")

    plt.title(f"Top 10 {column} Categories")
    plt.xlabel(column)
    plt.ylabel("Count")

    plt.xticks(rotation=45)

    plt.tight_layout()

    # Save category count plot
    plt.savefig(f"W1D4_top10_{column}.png")

    plt.show()


# --------------------------------------------------
# 7. EDA NARRATIVE
# --------------------------------------------------

print("\n" + "=" * 50)
print("EDA NARRATIVE")
print("=" * 50)

narrative = """
The dataset contains Indian sales records with customer IDs, cities,
products, and sales values. The dataset contains 14 records and 4
columns after the data cleaning performed in the previous task.
There are no missing values in the cleaned dataset.

The sales column is numerical and ranges from 15,000 to 65,000.
The average sales value is approximately 35,571. The distribution
plot helps identify how sales values are spread across different
ranges. The dataset contains different cities and products, and the
category count plots show their frequency.

The correlation heatmap shows the relationship between numerical
columns. However, customer_id is an identifier and should not normally
be treated as a meaningful numerical feature in machine learning.
Therefore, its correlation with sales should not be interpreted as a
business relationship.

The dataset was previously cleaned by removing duplicate records,
handling missing values, converting sales into numeric format, and
cleaning text fields. These steps make the dataset suitable for
further analysis.

One suspicious limitation is the very small dataset size. With only
14 records, the observed patterns may not represent real-world sales
behavior. Before using this data for machine learning, a larger and
more representative dataset should be collected. Additional checks
for outliers, inconsistent values, and useful feature relationships
should also be performed.
"""

print(narrative)

print("\nEDA completed successfully!")