class Student:
    school_name = "ABC College"

    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def display_student(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Course:", self.course)
        print("School Name:", Student.school_name)

    @classmethod
    def change_school_name(cls, new_name):
        cls.school_name = new_name

s1 = Student("Rahul", 18, "Computer Science")
s2 = Student("Priya", 19, "Information Technology")

print("Before Changing School Name:")
s1.display_student()
print()
s2.display_student()

Student.change_school_name("XYZ College")

print("\nAfter Changing School Name:")
s1.display_student()
print()
s2.display_student()