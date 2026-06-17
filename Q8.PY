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