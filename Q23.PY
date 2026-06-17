class School:
    school_name = "ABC School"

    def __init__(self, student):
        self.student = student

    @classmethod
    def change_school(cls, name):
        cls.school_name = name

    def display(self):
        print(self.student, School.school_name)

s = School("Rahul")
s.display()