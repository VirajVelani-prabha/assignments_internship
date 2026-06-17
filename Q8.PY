class Product:
    tax_rate = 18

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def final_price(self):
        total = self.price + (self.price * Product.tax_rate / 100)
        print("Product:", self.name)
        print("Final Price:", total)

p1 = Product("Laptop", 50000)

p1.final_price()