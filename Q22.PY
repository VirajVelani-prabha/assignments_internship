class Hospital:
    def __init__(self, name):
        self.name = name

class Doctor(Hospital):
    def display(self):
        print("Doctor:", self.name)

d = Doctor("Dr. Sharma")
d.display()