class Product:
    def __init__(self, name):
        self.name = name

class Mobile(Product):
    def display(self):
        print("Product:", self.name)

m = Mobile("iPhone")
m.display()