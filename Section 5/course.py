class Course:
    def __init__(self, course_name, duration, fees):
        self.course_name = course_name
        self.duration = duration
        self.fees = fees

    def display(self):
        print("Course Name:", self.course_name)
        print("Duration:", self.duration)
        print("Fees:", self.fees)

c1 = Course("Python Programming", "3 Months", 15000)

c1.display()