class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def display(self):
        print("Name:", self.name)

s = Student("Rahul")
s.display()