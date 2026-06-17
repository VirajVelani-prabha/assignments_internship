
class Product:
    def __init__(self, product_id, product_name, price):
        self.product_id = product_id
        self.product_name = product_name
        self.price = price

    def display(self):
        print("Product ID:", self.product_id)
        print("Product Name:", self.product_name)
        print("Price:", self.price)
        


p1 = Product(101, "Laptop", 50000)
p2 = Product(102, "Mobile", 20000)
p3 = Product(103, "Headphones", 1500)

print("Product 1 Details")
p1.display()

print("\nProduct 2 Details")
p2.display()

print("\nProduct 3 Details")
p3.display()