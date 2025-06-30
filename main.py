import pandas as pd
import matplotlib.pyplot as plt

# 1. Load CSV
df = pd.read_csv(r"C:\Users\Lenovo\Downloads\Walmart_Sales.csv")
df.columns = df.columns.str.strip()  # Clean whitespace

# 2. Explore the data
print("Columns:", df.columns.tolist())
print("\nFirst 5 rows:\n", df.head())
print("\nData types:\n", df.dtypes)
print("\nMissing values:\n", df.isnull().sum())
print("\nSummary statistics:\n", df.describe())

# 3. Convert Date to datetime and extract Month
df["Date"] = pd.to_datetime(df["Date"], dayfirst=True)
df["Month"] = df["Date"].dt.to_period("M")


# 4. Total Sales by Store
sales_by_store = df.groupby("Store")["Weekly_Sales"].sum()
print("\nTotal Sales by Store:\n", sales_by_store)

# 5. Monthly Sales Trend (all stores)
monthly_sales = df.groupby("Month")["Weekly_Sales"].sum()
print("\nMonthly Sales:\n", monthly_sales)

# 6. Sales on Holidays vs Non-Holidays
holiday_sales = df.groupby("Holiday_Flag")["Weekly_Sales"].mean()
print("\nAverage Sales: Holiday (1) vs Non-Holiday (0):\n", holiday_sales)

# 7. Visualization

# Bar chart: Sales by Store
sales_by_store.plot(kind="bar", figsize=(10, 6), title="Total Sales by Store", color='skyblue')
plt.xlabel("Store")
plt.ylabel("Total Weekly Sales")
plt.tight_layout()
plt.show()

# Line chart: Monthly Sales Trend
monthly_sales.plot(kind="line", marker='o', figsize=(10, 6), title="Monthly Sales Trend", color='green')
plt.xlabel("Month")
plt.ylabel("Total Weekly Sales")
plt.grid(True)
plt.tight_layout()
plt.show()

# Bar chart: Holiday vs Non-Holiday Sales
holiday_sales.plot(kind="bar", color=['orange', 'purple'], title="Average Sales: Holiday vs Non-Holiday")
plt.xticks(ticks=[0,1], labels=["Non-Holiday", "Holiday"], rotation=0)
plt.ylabel("Average Weekly Sales")
plt.tight_layout()
plt.show()

# 8. Final Insights
top_store = sales_by_store.idxmax()
top_sales = sales_by_store.max()
print(f"\n📈 Store with highest total sales: Store {top_store} with ${top_sales:,.2f}")
if holiday_sales[1] > holiday_sales[0]:
    print("🎉 Holiday weeks have higher average sales.")
else:
    print("📅 Non-holiday weeks have higher average sales.")
