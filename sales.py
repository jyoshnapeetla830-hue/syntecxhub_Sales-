import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

sns.set_style("whitegrid")

# --------------------------------
# Load Dataset (with error handling)
# --------------------------------
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "sales_data.csv")

if not os.path.exists(file_path):
    print("❌ File not found. Make sure 'sales_data.csv' exists.")
    exit()

df = pd.read_csv(file_path)

# --------------------------------
# Data Preprocessing
# --------------------------------
df['Date'] = pd.to_datetime(df['Date'])
df['Revenue'] = df['Quantity'] * df['Price']
df['Month'] = df['Date'].dt.to_period('M')

# --------------------------------
# KPIs
# --------------------------------
total_revenue = df['Revenue'].sum()
total_orders = df['OrderID'].nunique()
avg_order_value = total_revenue / total_orders

print("\n" + "="*45)
print("📊 SALES ANALYSIS DASHBOARD")
print("="*45)

print(f"Total Revenue       : ₹{total_revenue}")
print(f"Total Orders        : {total_orders}")
print(f"Average Order Value : ₹{avg_order_value:.2f}")

# --------------------------------
# Analysis
# --------------------------------
top_products = df.groupby('Product')['Revenue'].sum().sort_values(ascending=False)
top_regions = df.groupby('Region')['Revenue'].sum().sort_values(ascending=False)
monthly_sales = df.groupby('Month')['Revenue'].sum()
category_sales = df.groupby('Category')['Revenue'].sum()

print("\n🏆 Top Products:\n", top_products)
print("\n🌍 Top Regions:\n", top_regions)

# --------------------------------
# Business Insights (AUTO)
# --------------------------------
print("\n💡 Key Insights:")

print(f"- Best selling product: {top_products.idxmax()}")
print(f"- Top performing region: {top_regions.idxmax()}")
print(f"- Highest revenue category: {category_sales.idxmax()}")

# --------------------------------
# Save Charts Folder
# --------------------------------
os.makedirs("charts", exist_ok=True)

# --------------------------------
# Visualization + Save
# --------------------------------

# 1. Top Products
plt.figure(figsize=(8,5))
sns.barplot(x=top_products.index, y=top_products.values)
plt.title("Top Products by Revenue")
plt.xticks(rotation=30)
plt.tight_layout()
plt.savefig("charts/top_products.png")
plt.show()

# 2. Top Regions
plt.figure(figsize=(6,4))
sns.barplot(x=top_regions.index, y=top_regions.values)
plt.title("Revenue by Region")
plt.tight_layout()
plt.savefig("charts/top_regions.png")
plt.show()

# 3. Monthly Trend
plt.figure(figsize=(8,5))
monthly_sales.plot(marker='o')
plt.title("Monthly Sales Trend")
plt.grid()
plt.tight_layout()
plt.savefig("charts/monthly_sales.png")
plt.show()

# 4. Category Distribution
plt.figure(figsize=(6,6))
plt.pie(category_sales, labels=category_sales.index, autopct='%1.1f%%')
plt.title("Sales by Category")
plt.savefig("charts/category_distribution.png")
plt.show() 