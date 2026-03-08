import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Product": ["Laptop", "Mobile", "Tablet", "Laptop", "Mobile", "Tablet"],
    "Region": ["South", "North", "East", "West", "South", "North"],
    "Sales": [50000, 30000, 20000, 55000, 35000, 25000]
}

df = pd.DataFrame(data)

print("Dataset")
print(df)

print("\nDataset Info")
print(df.info())

print("\nStatistical Summary")
print(df.describe())

product_sales = df.groupby("Product")["Sales"].sum()
print("\nTotal Sales by Product")
print(product_sales)

region_sales = df.groupby("Region")["Sales"].sum()
print("\nTotal Sales by Region")
print(region_sales)

product_sales.plot(kind="bar")

plt.title("Total Sales by Product")
plt.xlabel("Product")
plt.ylabel("Sales")

plt.show()
