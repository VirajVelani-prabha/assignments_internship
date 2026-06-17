
class College:
    def __init__(self, college_name, city, students_count):
        self.college_name = college_name
        self.city = city
        self.students_count = students_count

    def display(self):
        print("College Name:", self.college_name)
        print("City:", self.city)
        print("Students Count:", self.students_count)

college1 = College("Zeal College", "Pune", 5000)
college2 = College("JSPM College", "Pune", 8000)

print("College 1 Details")
college1.display()

print("\nCollege 2 Details")
college2.display()