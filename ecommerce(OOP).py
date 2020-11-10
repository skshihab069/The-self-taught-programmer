# here i have created a program that tracks the inventory and purchases of customer

class Customer:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.purchases = []

    def purchase(self, inventory, products):
        inventory_dict = inventory.inventory
        if products in inventory_dict:
            if inventory_dict[products] > 0:
                self.purchases.append(products)
                inventory_dict[products] -= 1
            else:
                print("we are out of stock")
        else:
            print("We don,t have that product")

    def print_purchases(self):
        print("The customer purchased")
        for item in self.purchases:
            print(item.name)


class Products:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Inventory:
    def __init__(self):
        self.inventory = {}

    def add_products(self, products, quantity):
        if products not in self.inventory:
            self.inventory[products] = quantity
        else:
            self.inventory[products] += quantity

    def print_inventory(self):
        print("The Inventory has the following items")
        for key, value in self.inventory.items():
            print(key.name + ":" + str(value))
        print()


customer = Customer("Shihab", "skshihab069@gmail.com")
# print(customer.name)
# print(customer.email)

apple_watch = Products("APPLe", 2000)
# print(apple_watch.name)
# print(apple_watch.price)

mac_products = Products("mac books", 2300)
# print(mac_products.name)
# print(mac_products.price)

inventory = Inventory()
inventory.add_products(apple_watch, 200)
inventory.add_products(mac_products, 100)
inventory.print_inventory()
customer.purchase(inventory, apple_watch)
customer.print_purchases()
inventory.print_inventory()
