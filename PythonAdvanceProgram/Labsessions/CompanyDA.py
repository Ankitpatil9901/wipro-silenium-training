import pandas as pd

#Load data using pandas.
df = pd.read_csv("year_sale_data.csv")
print(df)

#Convert Date to datetime.
df['Date'] = pd.to_datetime(df['Date'])
print(df)

# Create new column
df['TotalSales'] = df['Quantity'] * df['Price']
print(df)

# Check null values
print(df.isnull().sum())

# handling null values
df.fillna(0, inplace=True)
#print(df)

# Region with highest total revenue
print(df.groupby('Region')['TotalSales'].sum().idxmax())

# Monthly sales
monthly_sales = df.groupby(df['Date'].dt.month)['TotalSales'].sum()

for month, sales in monthly_sales.items():
    print(f"Month {month}: {sales}")

# Best performing category
print(df.groupby('Category')['TotalSales'].sum().idxmax())

# Top 5 products by revenue
print(df.groupby('Product')['TotalSales'].sum().sort_values(ascending=False).head(5))


#-------------------Visualisation--------------------------------------------------------

import matplotlib.pyplot as plt

# Bar Chart -- Revenue by Region
region_rev = df.groupby('Region')['TotalSales'].sum()
region_rev.plot(kind='bar')
plt.title("Revenue by Region")
plt.xlabel("Region")
plt.ylabel("Total Revenue")
plt.show()


#line plt ---  Monthly Revenue Trend
monthly_rev = df.groupby(df['Date'].dt.month)['TotalSales'].sum()
monthly_rev.plot(kind='line', marker='o')
plt.title("Monthly Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Total Revenue")
plt.show()


# pie chart --Category Contribution
cat_rev = df.groupby('Category')['TotalSales'].sum()
cat_rev.plot(kind='pie', autopct='%1.1f%%')
plt.title("Category Contribution")
plt.ylabel("Category Share")
plt.show()


# horizontal bar graph -- Top 5 Products
top_products = df.groupby('Product')['TotalSales'].sum().sort_values(ascending=False).head(5)
top_products.plot(kind='barh')
plt.title("Top 5 Products by Revenue")
plt.xlabel("Total Revenue")
plt.ylabel("Product")
plt.show()