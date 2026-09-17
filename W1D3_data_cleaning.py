import pandas as pd

# --------------------------------------------------
# 1. LOAD DATA
# --------------------------------------------------

# Load the CSV dataset
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

# Remove extra spaces and convert column names to lowercase
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

print("\nCleaned Column Names:")
print(df.columns.tolist())


# --------------------------------------------------
# 3. REMOVE DUPLICATE ROWS
# --------------------------------------------------

# Remove duplicate records
duplicates = df.duplicated().sum()

print("\nDuplicate Rows:", duplicates)

df = df.drop_duplicates()


# --------------------------------------------------
# 4. HANDLE MISSING VALUES
# --------------------------------------------------

# Fill missing numerical values with the column median
df["sales"] = df["sales"].fillna(df["sales"].median())

# Fill missing city values with "Unknown"
df["city"] = df["city"].fillna("Unknown")

# Fill missing product values with "Unknown"
df["product"] = df["product"].fillna("Unknown")


# --------------------------------------------------
# 5. CLEAN TEXT DATA
# --------------------------------------------------

# Remove unnecessary spaces from text columns
df["city"] = df["city"].str.strip()
df["product"] = df["product"].str.strip()


# --------------------------------------------------
# 6. INSPECT CLEANED DATA
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
# 7. BASIC STATISTICS
# --------------------------------------------------

print("\nSales Statistics:")
print(df["sales"].describe())


# --------------------------------------------------
# 8. SAVE CLEANED DATA
# --------------------------------------------------

df.to_csv("W1D3_indian_sales_cleaned.csv", index=False)

print("\nCleaned dataset saved successfully!")
print("File: W1D3_indian_sales_cleaned.csv")