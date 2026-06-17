

class Laptop:
    def __init__(self, brand, ram, price):
        self.brand = brand
        self.ram = ram
        self.price = price

laptop1 = Laptop("Dell", "8 GB", 50000)
laptop2 = Laptop("HP", "16 GB", 65000)

print("Laptop 1")
print("Brand:", laptop1.brand)
print("RAM:", laptop1.ram)
print("Price:", laptop1.price)

print("\nLaptop 2")
print("Brand:", laptop2.brand)
print("RAM:", laptop2.ram)
print("Price:", laptop2.price)