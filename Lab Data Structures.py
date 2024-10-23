# Exercise: Managing Customer Orders

# Step 1: Define the list of products
products = ["t-shirt", "mug", "hat", "book", "keychain"]  # Use lowercase 'products' to keep it consistent

# Step 2: Create an empty dictionary for inventory
dict_inventory = {}

# Loop through each product to ask for quantities
for product in products:
    while True:
        try:
            # Ask the user to input the quantity of each product
            quantity = int(input(f"What is the quantity of {product}: "))  # Use 'product' here, not 'Product'
            # Store the quantity of a product inside the inventory dictionary
            dict_inventory[product] = quantity
            break  # Exit the loop if a valid quantity is entered
        except ValueError:
            print("Please enter a valid number.")  # Handle invalid input

# Create an empty set for customer orders
customer_orders = set()  # Fixed variable name to 'customer_orders'

# Ask the user for three product orders
for i in range(3):  # Create a defined loop for three orders
    order = input(f"What is the order of product {i + 1}: ")  # Clarified prompt message
    if order in products:
        customer_orders.add(order)  # Add valid orders to the set
    else:
        print("Invalid product, please choose from the list.")

# Print the customer orders
print("\nCustomer orders:", customer_orders)  # Fixed syntax to use a comma

# Calculate order statistics
total_products_ordered = len(customer_orders)  # Calculate total unique products ordered
percentage_ordered = (total_products_ordered / len(products)) * 100  # Calculate percentage
order_status = (total_products_ordered, percentage_ordered)  # Create a tuple for order status

# Print the order statistics
print("Order Statistics:")  # Print header
print(f"Total Products Ordered: {total_products_ordered}")  # Total ordered products
print(f"Percentage of Products Ordered: {percentage_ordered:.2f}%")  # Formatted percentage to 2 decimal places

# Update the inventory by subtracting 1 from the quantity of each product in customer orders
for product in customer_orders:
    if product in dict_inventory:  # Check if the product exists in inventory
        dict_inventory[product] -= 1  # Subtract 1 from the inventory
    else:
        print(f"{product} not found in inventory.")  # Handle case if product is not found

# Print the updated inventory
print("\nUpdated Inventory:")
for product, quantity in dict_inventory.items():
    print(f"{product}: {quantity} units available")  # Display each product and its quantity


#displaying the quantity of each product on separate lines.
print("\nUpdated Inventory:") #when this line is executed, it will first move the cursor to a new line before printing "Updated Inventory
for product, quantity in dict_inventory.items():
    print(f"{product}: {quantity} units available")