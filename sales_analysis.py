import pandas as pd

# Load sales data
df = pd.read_csv("sales_data.csv")

# Basic information
print("Sales Data Overview")
print(df.head())

# Total revenue
total_revenue = df["Revenue"].sum()
print("\nTotal Revenue:", total_revenue)

# Total quantity sold
total_quantity = df["Quantity"].sum()
print("Total Quantity Sold:", total_quantity)

# Revenue by product
product_sales = df.groupby("Product")["Revenue"].sum().sort_values(ascending=False)

print("\nRevenue by Product:")
print(product_sales)

# Revenue by region
region_sales = df.groupby("Region")["Revenue"].sum().sort_values(ascending=False)

print("\nRevenue by Region:")
print(region_sales)

# Monthly revenue
df["Date"] = pd.to_datetime(df["Date"])
monthly_sales = df.groupby(df["Date"].dt.to_period("M"))["Revenue"].sum()

print("\nMonthly Revenue:")
print(monthly_sales)