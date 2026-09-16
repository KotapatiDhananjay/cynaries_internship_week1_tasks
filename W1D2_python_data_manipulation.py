import pandas as pd
import os

# --------------------------------------------------
# 1. LOAD DATASET
# --------------------------------------------------

# Load Indian sales dataset
sales = pd.read_csv("W1D2_Indian_Sales.csv")

print("Dataset Shape:", sales.shape)
print("\nData Types:")
print(sales.dtypes)

print("\nFirst 10 Rows:")
print(sales.head(10))


# --------------------------------------------------
# 2. FILTER OPERATION
# --------------------------------------------------

# Filter sales where the sales amount is greater than 5000
filtered_sales = sales[sales["Sales"] > 5000]

print("\nFiltered Sales (Sales > 5000):")
print(filtered_sales)


# --------------------------------------------------
# 3. GROUPBY OPERATION
# --------------------------------------------------

# Group data by city and calculate total sales
city_sales = sales.groupby("City")["Sales"].sum().reset_index()

print("\nTotal Sales by City:")
print(city_sales)


# --------------------------------------------------
# 4. MERGE OPERATION
# --------------------------------------------------

# Load customer information
customers = pd.read_csv("W1D2_indian_customers.csv")

# Merge sales and customer data using Customer_ID
merged_data = pd.merge(
    sales,
    customers,
    on="Customer_ID",
    how="inner"
)

print("\nMerged Data:")
print(merged_data)


# --------------------------------------------------
# 5. PIVOT TABLE
# --------------------------------------------------

# Create a pivot table showing total sales by city and product
pivot = pd.pivot_table(
    sales,
    values="Sales",
    index="City",
    columns="Product",
    aggfunc="sum",
    fill_value=0
)

print("\nPivot Table:")
print(pivot)


# --------------------------------------------------
# 6. EXPORT CLEANED DATA
# --------------------------------------------------

# Save cleaned/merged data as CSV
merged_data.to_csv("cleaned_sales.csv", index=False)

# Save cleaned/merged data as Parquet
merged_data.to_parquet("cleaned_sales.parquet", index=False)

print("\nFiles exported successfully.")


# --------------------------------------------------
# 7. COMPARE FILE SIZES
# --------------------------------------------------

csv_size = os.path.getsize("cleaned_sales.csv")
parquet_size = os.path.getsize("cleaned_sales.parquet")

print("\nFile Size Comparison:")
print(f"CSV Size: {csv_size} bytes")
print(f"Parquet Size: {parquet_size} bytes")

if csv_size > parquet_size:
    print("Parquet file is smaller.")
elif parquet_size > csv_size:
    print("CSV file is smaller.")
else:
    print("Both files have the same size.")