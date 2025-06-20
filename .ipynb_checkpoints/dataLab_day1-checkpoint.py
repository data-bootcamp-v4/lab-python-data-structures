
#As part of a business venture, you are starting an online store that sells various products. To ensure smooth operations, you need to develop a program that manages customer orders and inventory.
#Follow the steps below to complete the exercise:

#1. Define a list called `products` that contains the following items: "t-shirt", "mug", "hat", "book", "keychain".
products = ["t-shirt", "mug", "hat", "book", "keychain"]

#2. Create an empty dictionary called `inventory`.
inventory={}

#3. Ask the user to input the quantity of each product available in the inventory. 
#Use the product names from the `products` list as keys in the `inventory` dictionary and assign the respective quantities as values.#
for product in products:
    num = float(input(f'Enter a quantity for {product}:'))
    inventory[product]=num  #dictionary enters all the values for each key provided
print('The dicctionary called inventory is:' ,inventory)    

#4. Create an empty set called `customer_orders`.
customer_orders = set()
#5. Ask the user to input the name of three products that a customer wants to order (from those in the products list, meaning three products out of "t-shirt", "mug", "hat", "book" or "keychain". Add each product name to the `customer_orders` set.

for i in range(3):
    product = input("Enter the name of a product to order (t-shirt, mug, hat, book, keychain): ")
    if product in products:
        customer_orders.add(product)
    else:
        print("Invalid product. Please choose from the available products.")

#6. Print the products in the `customer_orders` set.
print("Customer orders:", customer_orders)

#7. Calculate the following order statistics:
   #- Total Products Ordered: The total number of products in the `customer_orders` set.
total_customers_ordered = len(customer_orders)
   #- Percentage of Products Ordered: The percentage of products ordered compared to the total available products.
percentage_ordered= (total_customers_ordered/len(products))
   #Store these statistics in a tuple called `order_status`.
order_status =(total_customers_ordered,percentage_ordered)

#8. Print the order statistics using the following format:
   #Order Statistics:
   #Total Products Ordered: <total_products_ordered>
   #Percentage of Products Ordered: <percentage_ordered>% 
print('The total of customers ordered:' , total_customers_ordered)
print('The percentage is: ', percentage_ordered)

#9. Update the inventory by subtracting 1 from the quantity of each product. Modify the `inventory` dictionary accordingly.
#inventory=inventory[:-1]


#10. Print the updated inventory, displaying the quantity of each product on separate lines.
#print(inventory)
#Solve the exercise by implementing the steps using the Python concepts of lists, dictionaries, sets, and basic input/output operations. 