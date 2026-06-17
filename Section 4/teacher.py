class Teacher:
    def __init__(self, teacher_name, subject):
        self.teacher_name = teacher_name
        self.subject = subject

    def display(self):
        print("Teacher Name:", self.teacher_name)
        print("Subject:", self.subject)

t1 = Teacher("Rahul Sharma", "Mathematics")

t1.display()