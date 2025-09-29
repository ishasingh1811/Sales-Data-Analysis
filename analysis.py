import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load CSV file
df = pd.read_csv("sales.csv")

# Display first 5 rows
print("First 5 rows of dataset:")
print(df.head())

# Step 2: Basic info
print("\nDataset Info:")
print(df.info())

print("\nSummary Statistics:")
print(df.describe())

# Step 3: Group by Product - total sales
df["Total_Sales"] = df["Quantity"] * df["Price"]

sales_by_product = df.groupby("Product")["Total_Sales"].sum().sort_values(ascending=False)
print("\nTotal Sales by Product:")
print(sales_by_product)

# Step 4: Plot - Sales by Product
plt.figure(figsize=(8,5))
sales_by_product.plot(kind="bar", color="skyblue")
plt.title("Total Sales by Product")
plt.xlabel("Product")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.show()

# Step 5: Group by Date - sales trend
sales_by_date = df.groupby("Date")["Total_Sales"].sum()

plt.figure(figsize=(10,5))
sales_by_date.plot(kind="line", marker="o")
plt.title("Sales Trend Over Time")
plt.xlabel("Date")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.show()

print("\nOutcome: Basic data insights using Python completed ✅")
