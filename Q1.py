# Base Class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Derived Class 1
class Student(Person):
    def __init__(self, name, age, roll_no):
        Person.__init__(self, name, age)
        self.roll_no = roll_no

# Derived Class 2
class Teacher(Person):
    def __init__(self, name, age, subject):
        Person.__init__(self, name, age)
        self.subject = subject

# Hybrid Inheritance (Multiple Inheritance)
class TeachingAssistant(Student, Teacher):
    def __init__(self, name, age, roll_no, subject):
        Student.__init__(self, name, age, roll_no)
        self.subject = subject

    def display(self):
        print("----- Teaching Assistant Details -----")
        print("Name :", self.name)
        print("Age :", self.age)
        print("Roll No :", self.roll_no)
        print("Subject :", self.subject)

# Main Program
ta = TeachingAssistant("Viraj", 18, 101, "Python Programming")
ta.display()