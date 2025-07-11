import pandas as pd

# Load Kaggle sales data
df = pd.read_csv('sales_data_sample.csv', encoding='ISO-8859-1')


# View basic info
print(df.head())
print(df.info())
# Drop rows with missing important values
df = df.dropna(subset=['PRODUCTLINE', 'ORDERDATE', 'QUANTITYORDERED', 'PRICEEACH'])


# Convert columns to correct datatypes
df['QUANTITYORDERED'] = pd.to_numeric(df['QUANTITYORDERED'], errors='coerce')
df['PRICEEACH'] = pd.to_numeric(df['PRICEEACH'], errors='coerce')
df['ORDERDATE'] = pd.to_datetime(df['ORDERDATE'], errors='coerce')
df = df[(df['QUANTITYORDERED'] > 0) & (df['PRICEEACH'] > 0)]
df['Total_Sales'] = df['QUANTITYORDERED'] * df['PRICEEACH']

# Remove rows with invalid or zero quantity/price


# Create total sales column

df.to_csv('Cleaned_RetailSales.csv', index=False)
print("✅ Cleaned data saved to 'Cleaned_RetailSales.csv'")
import matplotlib.pyplot as plt

# Group by product
sales_by_product = df.groupby('PRODUCTLINE')['Total_Sales'].sum().sort_values(ascending=False)


# Plot
plt.figure(figsize=(10, 6))
sales_by_product.plot(kind='bar', color='teal')
plt.title('Total Sales per Product')
plt.xlabel('Product')
plt.ylabel('Sales Amount')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
from sqlalchemy import create_engine

# Save to SQLite database
engine = create_engine('sqlite:///retail_sales.db')
df.to_sql('sales_data', con=engine, if_exists='replace', index=False)

print("📦 Data saved to SQLite database: retail_sales.db")
