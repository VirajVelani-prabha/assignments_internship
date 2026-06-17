<<<<<<< HEAD
class Shape:
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        print("Area of Circle =", 3.14 * self.radius * self.radius)


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        print("Area of Rectangle =", self.length * self.width)


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        print("Area of Square =", self.side * self.side)


c = Circle(5)
r = Rectangle(10, 4)
s = Square(6)

c.area()
r.area()
s.area()
=======
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
>>>>>>> 311fd1035d158aae48cdc680a3b52c4edde99c26
