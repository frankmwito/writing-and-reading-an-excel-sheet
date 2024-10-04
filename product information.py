from openpyxl import Workbook

# Create a new workbook and select the active worksheet
wb = Workbook()
ws = wb.active

# Add headers to the worksheet
ws.append(["Product Name", "Price", "Quantity (kg)", "Company"])

# List to store product information
product_inventory = []

# Get the number of products from the user
num_of_products = int(input("Enter the maximum number of products: "))

# Loop to collect product details
for i in range(num_of_products):
    product_name = input(f"Enter product name {i+1}: ")
    price = float(input(f"Enter product price {i+1}: "))
    quantity = input(f"Enter quantity in (kg) for product {i+1}: ")
    company = input(f"Enter company's name for product {i+1}: ")
    product_inventory.append([product_name, price, quantity, company])  # Append as a list

# Write data to the worksheet
for data in product_inventory:
    ws.append(data)

# Save the Excel file
wb.save("product_inventory.xlsx")

print("Product_inventory Excel file has been created successfully.")
