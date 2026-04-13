"c:\Users\MEL\Downloads\DATA\laboratorio1\Untitled-1.py"

# Step 1: Define the products list
from doctest import master

products = ["t-shirt", "mug", "hat", "book", "keychain"]

# Step 2: Create an empty inventory dictionary
inventory = {}

# Step 3: Ask the user for the quantity of each product
for product in products:
    quantity = int(input(f"Enter the quantity of {product}: "))
    inventory[product] = quantity

# Step 4: Create an empty set for customer orders
customer_orders = set()

# Step 5: Ask the user for the products they want to order
for i in range(3):  # Assuming the user can order up to 3 products
    order = input(f"Enter product {i+1} to order: ")
    customer_orders.add(order)

# Step 6: Print the customer orders 
print("\nCustomer Orders:", customer_orders)

# Step 7: Calculate order statistics
total_products_ordered = len(customer_orders)
percentage_ordered = (total_products_ordered / len(products)) * 100

# Store in a tuple
order_status = (total_products_ordered, percentage_ordered)

# Step 8: Print the order statistics
print("\nOrder Statistics:")
print(f"Total Products Ordered: {order_status[0]}")
print(f"Percentage of Products Ordered: {order_status[1]}%")

# Step 9: Update inventory by subtracting 1 from each product
for product in inventory:
      inventory[product] -= 1

# Step 10: Print the updated inventory
print("\nUpdated Inventory:")
for product, quantity in inventory.items():
      print(f"{product}: {quantity}")

git add .

git commit -m "Solved lab"

git push origin master
