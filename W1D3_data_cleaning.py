import pandas as pd

# --------------------------------------------------
# 1. LOAD DATA
# --------------------------------------------------

# Load the Indian sales dataset
df = pd.read_csv("W1D3_indian_sales_dirty.csv")

print("ORIGINAL DATASET")
print("----------------")
print("Shape:", df.shape)

print("\nFirst 5 Rows:")
print(df.head())

print("\nData Types:")
print(df.dtypes)

print("\nMissing Values:")
print(df.isnull().sum())


# --------------------------------------------------
# 2. CLEAN COLUMN NAMES
# --------------------------------------------------

# Remove extra spaces and make column names lowercase
df.columns = (
    df.columns
    .str.strip()
    .str.lower()
    .str.replace(" ", "_")
)

print("\nCleaned Column Names:")
print(df.columns.tolist())


# --------------------------------------------------
# 3. CONVERT SALES TO NUMERIC
# --------------------------------------------------

# Convert sales values from string to numeric
# Invalid values will become NaN
df["sales"] = pd.to_numeric(df["sales"], errors="coerce")

print("\nData Types After Conversion:")
print(df.dtypes)


# --------------------------------------------------
# 4. REMOVE DUPLICATE ROWS
# --------------------------------------------------

# Count duplicate rows
duplicates = df.duplicated().sum()

print("\nDuplicate Rows:", duplicates)

# Remove duplicate rows
df = df.drop_duplicates()


# --------------------------------------------------
# 5. HANDLE MISSING VALUES
# --------------------------------------------------

# Fill missing sales values with the median sales
df["sales"] = df["sales"].fillna(df["sales"].median())

# Fill missing city values with "Unknown"
df["city"] = df["city"].fillna("Unknown")

# Fill missing product values with "Unknown"
df["product"] = df["product"].fillna("Unknown")


# --------------------------------------------------
# 6. CLEAN TEXT DATA
# --------------------------------------------------

# Remove unnecessary spaces from city and product
df["city"] = df["city"].str.strip()
df["product"] = df["product"].str.strip()


# --------------------------------------------------
# 7. INSPECT CLEANED DATA
# --------------------------------------------------

print("\nCLEANED DATASET")
print("---------------")

print("\nShape:", df.shape)

print("\nFirst 10 Rows:")
print(df.head(10))

print("\nData Types:")
print(df.dtypes)

print("\nMissing Values After Cleaning:")
print(df.isnull().sum())


# --------------------------------------------------
# 8. BASIC STATISTICS
# --------------------------------------------------

print("\nSales Statistics:")
print(df["sales"].describe())


# --------------------------------------------------
# 9. SAVE CLEANED DATASET
# --------------------------------------------------

df.to_csv("W1D3_indian_sales_cleaned.csv", index=False)

print("\nCleaned dataset saved successfully!")
print("File: W1D3_indian_sales_cleaned.csv")