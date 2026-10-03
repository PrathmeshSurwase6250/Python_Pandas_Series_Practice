import pandas as pd
# 1. Load the CSV
# Read the CSV using pd.read_csv() and store it in df.
data = pd.read_csv("/Users/prathmeshsurwase/Desktop/Pandas /SeriesPractise/csvFiles/ecommerce_sales_pandas_practice.csv")
data = data.squeeze("columns")
print(data)
# 2. Display Data
# Print:
# - First 5 rows
print(data.head())
# - Last 5 rows
print(data.tail())
# - First 10 rows
print(data.head(10))
# - Random 10 rows
print(data.sample(10))
# Methods to practice:
# head()tail()sample()


# 3. Understand the Dataset
# Find:

# - Number of rows
print(data.shape[0])
# - Number of columns
print(data.shape[1])
# - Column names
print(data.columns)
# - Data types
print(data.dtypes)
# - Basic statistics
print(data.describe())
# Practice:
# shapecolumnsdtypesinfo()describe()
data.info()

# 4. Select Columns
# Display:
# - product
print(data["product"])
# - city
print(data["city"])
# - quantity
print(data["quantity"])
# - unit_price
print(data["unit_price"])
# Then select:
# - order_id
print(data["order_id"])
# - product
print(data["product"])
# - customer_rating
print(data["customer_rating"])
# 5. Select Rows
# Using iloc, display:
# - First row
print(data.iloc[0])
# - 10th row
print(data.iloc[9])
# - Rows 10–20
print(data.iloc[9 : 20])
# - Last 10 rows
print(data.iloc[-10 : ])