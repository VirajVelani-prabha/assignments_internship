class Shape:
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def area(self):
        print("Area of Circle =", 3.14 * self.r * self.r)


class Rectangle(Shape):
    def __init__(self, l, b):
        self.l = l
        self.b = b

    def area(self):
        print("Area of Rectangle =", self.l * self.b)


class Triangle(Shape):
    def __init__(self, b, h):
        self.b = b
        self.h = h

    def area(self):
        print("Area of Triangle =", 0.5 * self.b * self.h)


shapes = [Circle(5), Rectangle(4, 6), Triangle(8, 5)]

for shape in shapes:
    shape.area()