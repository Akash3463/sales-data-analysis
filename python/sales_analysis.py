import pandas as pd

# Load sales data
df = pd.read_csv("data/sales_data.csv")

print("SALES DATA ANALYSIS")
print("=" * 40)

# Basic information
print("\nFirst 5 Records:")
print(df.head())

# Total revenue
total_revenue = df["Revenue"].sum()
print(f"\nTotal Revenue: ₹{total_revenue:,.2f}")

# Total quantity
total_quantity = df["Quantity"].sum()
print(f"Total Quantity Sold: {total_quantity}")

# Average revenue
average_revenue = df["Revenue"].mean()
print(f"Average Revenue per Transaction: ₹{average_revenue:,.2f}")

# Revenue by product
product_sales = (
    df.groupby("Product")["Revenue"]
    .sum()
    .sort_values(ascending=False)
)

print("\nRevenue by Product:")
print(product_sales)

# Revenue by region
region_sales = (
    df.groupby("Region")["Revenue"]
    .sum()
    .sort_values(ascending=False)
)

print("\nRevenue by Region:")
print(region_sales)

# Monthly revenue
df["Date"] = pd.to_datetime(df["Date"])

monthly_sales = (
    df.groupby(df["Date"].dt.to_period("M"))["Revenue"]
    .sum()
)

print("\nMonthly Revenue:")
print(monthly_sales)

print("\nAnalysis completed successfully.")