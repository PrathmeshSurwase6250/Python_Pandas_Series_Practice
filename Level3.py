import pandas as pd
# 1. Load the CSV
# Read the CSV using pd.read_csv() and store it in df.
data = pd.read_csv("/Users/prathmeshsurwase/Desktop/Pandas /SeriesPractise/csvFiles/ecommerce_sales_pandas_practice.csv")
data = data.squeeze("columns")
print(data)
# 🟡 LEVEL 3 — Sorting & Ranking
# 13. Sort by Price
# Sort products from:
# Highest → Lowest price
print(data.sort_values("unit_price", ascending=False))
# 14. Sort by Quantity
# Find the 10 orders with the highest quantity.
print(data.sort_values("unit_price", ascending=False).head(10))
# 15. Top 10 Expensive Products
# Display:
# product
# unit_price
# city
# for the 10 most expensive orders.
print(data.sort_values("unit_price", ascending=False).head(10)[["product" , "unit_price" , "city"]])
# 16. Lowest Rated Orders
# Find the 10 orders with the lowest customer rating.
print(data.sort_values("customer_rating" ).head(10))
# 17. Multiple Sorting
# Sort by:
# city ascending
# unit_price descending
values = ["city" , "unit_price"]
print(data.sort_values(values ,    ascending=[True, False]))