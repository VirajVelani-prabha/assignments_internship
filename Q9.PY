<<<<<<< HEAD
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
=======
class Student:
    school_name = "ABC School"

    def __init__(self, name):
        self.name = name

    @classmethod
    def update_school_name(cls, new_name):
        cls.school_name = new_name

    def display(self):
        print("Name:", self.name)
        print("School:", Student.school_name)

s1 = Student("Rahul")
s2 = Student("Priya")

Student.update_school_name("XYZ School")

s1.display()
s2.display()
>>>>>>> 311fd1035d158aae48cdc680a3b52c4edde99c26
