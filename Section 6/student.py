class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def calculate_percentage(self):
        percentage = (self.marks / 500) * 100
        print("Name:", self.name)
        print("Percentage:", percentage, "%")

s1 = Student("Rahul", 425)

s1.calculate_percentage()