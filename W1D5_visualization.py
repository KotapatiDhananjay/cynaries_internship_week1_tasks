import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# --------------------------------------------------
# 1. LOAD DATA
# --------------------------------------------------

df = pd.read_csv("W1D3_indian_sales_cleaned.csv")

print("=" * 50)
print("W1D5 - DATA VISUALISATION")
print("=" * 50)

print("\nDataset Shape:")
print(df.shape)

print("\nFirst 5 Rows:")
print(df.head())


# --------------------------------------------------
# 2. SALES DISTRIBUTION
# --------------------------------------------------

plt.figure(figsize=(8, 5))

sns.histplot(
    df["sales"],
    bins=8,
    kde=True
)

plt.title("Sales Distribution")
plt.xlabel("Sales")
plt.ylabel("Frequency")

plt.tight_layout()

plt.savefig("W1D5_sales_distribution.png")

plt.show()


# --------------------------------------------------
# 3. SALES BY CITY
# --------------------------------------------------

city_sales = df.groupby("city")["sales"].sum().sort_values(
    ascending=False
)

plt.figure(figsize=(8, 5))

city_sales.plot(kind="bar")

plt.title("Total Sales by City")
plt.xlabel("City")
plt.ylabel("Total Sales")

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig("W1D5_sales_by_city.png")

plt.show()


# --------------------------------------------------
# 4. SALES BY PRODUCT
# --------------------------------------------------

product_sales = df.groupby("product")["sales"].sum().sort_values(
    ascending=False
)

plt.figure(figsize=(8, 5))

product_sales.plot(kind="bar")

plt.title("Total Sales by Product")
plt.xlabel("Product")
plt.ylabel("Total Sales")

plt.xticks(rotation=0)

plt.tight_layout()

plt.savefig("W1D5_sales_by_product.png")

plt.show()


# --------------------------------------------------
# 5. CORRELATION HEATMAP
# --------------------------------------------------

numeric_data = df.select_dtypes(include="number")

correlation = numeric_data.corr()

plt.figure(figsize=(7, 5))

sns.heatmap(
    correlation,
    annot=True,
    cmap="coolwarm",
    fmt=".2f"
)

plt.title("Correlation Heatmap")

plt.tight_layout()

plt.savefig("W1D5_correlation_heatmap.png")

plt.show()


# --------------------------------------------------
# 6. SALES TREND
# --------------------------------------------------

# Create transaction number to visualize sales progression
df["transaction_number"] = range(1, len(df) + 1)

plt.figure(figsize=(8, 5))

plt.plot(
    df["transaction_number"],
    df["sales"],
    marker="o"
)

plt.title("Sales by Transaction")
plt.xlabel("Transaction Number")
plt.ylabel("Sales")

plt.grid(True)

plt.tight_layout()

plt.savefig("W1D5_sales_trend.png")

plt.show()


# --------------------------------------------------
# 7. PRINT INSIGHTS
# --------------------------------------------------

print("\nVISUALISATION INSIGHTS")
print("----------------------")

print(
    f"Highest sales city: "
    f"{city_sales.idxmax()} "
    f"({city_sales.max():.2f})"
)

print(
    f"Highest sales product: "
    f"{product_sales.idxmax()} "
    f"({product_sales.max():.2f})"
)

print(
    f"Average sales: "
    f"{df['sales'].mean():.2f}"
)

print(
    f"Maximum single sale: "
    f"{df['sales'].max():.2f}"
)

print("\nAll visualisations created successfully!")