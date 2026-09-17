import pandas as pd

# Load the cleaned dataset
df = pd.read_csv("W1D3_indian_sales_cleaned.csv")

# Test 1: Dataset should not contain duplicate rows
assert df.duplicated().sum() == 0

# Test 2: Sales column should not contain missing values
assert df["sales"].isnull().sum() == 0

# Test 3: City column should not contain missing values
assert df["city"].isnull().sum() == 0

# Test 4: Product column should not contain missing values
assert df["product"].isnull().sum() == 0

# Test 5: Dataset should contain records
assert len(df) > 0

print("All tests passed successfully!")