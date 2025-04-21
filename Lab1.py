

products = ["t-shirt", "mug", "hat", "book", "keychain"]
inventory = {}
inventory["t-shirt"] = int(input("Quantity of t-shirt: "))
inventory["mug"] = int(input("Quantity of mug: "))
inventory["hat"] = int(input("Quantity of hat: "))
inventory["book"] = int(input("Quantity of book: "))
inventory["keychain"] = int(input("Quantity of keychain: "))



customers_order = {(input("De estos productos t-shirt, mug, hat, book, keychain , elige el producto numero1: ")) , 
(input("De estos productos t-shirt, mug, hat, book, keychain , elige el producto numero2: ")) , 
(input("De estos productos t-shirt, mug, hat, book, keychain , elige el producto numero3: "))
}

print(customers_order)


total_products = 10 + 10 + 10 + 10 + 10   #Suponemos que hay 10 unidades de cada item

total_costumers_order = 3
total_costumers_orderStr = str(total_costumers_order)

percetage_costumers_order = (total_costumers_order / total_products) * 100
percetage_costumers_orderStr = str(percetage_costumers_order)

order_status = (50, 3, "6%")

print("Order Statistics: \n" + "Total products ordered: " + total_costumers_orderStr + "\n" + "Percentage of product ordered: " + percetage_costumers_orderStr + "%")

inventory["t-shirt"] -= 1
inventory["mug"] -= 1
inventory["hat"] -= 1
inventory["book"] -= 1
inventory["keychain"] -= 1

print(inventory)
