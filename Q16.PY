class Shape:
    pass

class Circle(Shape):
    def area(self, r):
        print("Area:", 3.14 * r * r)

class Rectangle(Shape):
    def area(self, l, w):
        print("Area:", l * w)

c = Circle()
c.area(5)

r = Rectangle()
r.area(10, 5)