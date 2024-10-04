# Creating a list of products with prices in an excel spread sheet

from openpyxl import Workbook

# Create a new workbook and select the active worksheet
wb = Workbook()
ws = wb.active

# Add headers to the worksheet
ws.append(["Product", "Price"])

# Get the number of products from the user
number_of_products = int(input("Enter the maximum number of products: "))

# List to store products and prices
product_list = []

# Loop to collect product names and prices
for i in range(number_of_products):
    product = input(f"Enter product name {i+1}: ")
    price = float(input(f"Enter its price {i+1}: "))
    product_list.append([product, price])  # Append product and price as a list

# Write data to the worksheet
for data in product_list:
    ws.append(data)

# Save the Excel file
wb.save("products_and_prices.xlsx")

print("Excel file created with product names and prices!")
