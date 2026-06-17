class Hospital:
    def __init__(self, doctor_name, specialization):
        self.doctor_name = doctor_name
        self.specialization = specialization

    def display(self):
        print("Doctor Name:", self.doctor_name)
        print("Specialization:", self.specialization)

h1 = Hospital("Dr. Sharma", "Cardiologist")
h2 = Hospital("Dr. Patel", "Neurologist")
h3 = Hospital("Dr. Gupta", "Orthopedic")

h1.display()
print()

h2.display()
print()

h3.display()