class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)

s1 = Student("Rahul", 18)
s2 = Student("Priya", 19)
s3 = Student("Amit", 20)

s1.display()
print()

s2.display()
print()

s3.display()