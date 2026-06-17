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