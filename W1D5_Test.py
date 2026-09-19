import pandas as pd
import os

# Load dataset
df = pd.read_csv("W1D3_indian_sales_cleaned.csv")

# Test 1: Dataset should contain rows
assert len(df) > 0

# Test 2: Sales column should exist
assert "sales" in df.columns

# Test 3: City column should exist
assert "city" in df.columns

# Test 4: Product column should exist
assert "product" in df.columns

# Test 5: Sales should be numeric
assert pd.api.types.is_numeric_dtype(df["sales"])

print("All W1D5 tests passed successfully!")