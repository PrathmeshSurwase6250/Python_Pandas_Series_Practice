import pandas as pd
# 1. Load the CSV
# Read the CSV using pd.read_csv() and store it in df.
data = pd.read_csv("/Users/prathmeshsurwase/Desktop/Pandas /SeriesPractise/csvFiles/ecommerce_sales_pandas_practice.csv")
data = data.squeeze("columns")
print(data)
# 🟢 LEVEL 2 — Filtering
# 6. Pune Orders
# Find all orders where:
# city == Pune
print(data[data["city"] == "Pune"])

# 7. Expensive Products
# Find products where:
# unit_price > 30000
print(data[data["unit_price"] > 30000])
# 8. Large Orders
# Find orders where:
# quantity >= 4
print(data[data["quantity"] > 4])
# 9. Electronics Orders
# Find all orders from:
# category == Electronics
print(data[data["category"] == "Electronics"])
# 10. Multiple Conditions
# Find orders where:
# city == Pune
# AND
# quantity >= 3
print(data[(data["city"] == "Pune") & (data["quantity"] > 3)])

# 11. OR Condition
# Find orders where:
# category == Electronics
# OR
# category == Sports
print(data[(data["category"] == "Electronics") | (data["category"] == "Sports")])
# 12. Price Range
# Find products whose price is between:
# ₹10,000 and ₹30,000

print(data[data.unit_price.between(10000,30000)])