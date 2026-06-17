class Person:
    def __init__(self, name):
        self.name = name


class Doctor(Person):
    def treat_patient(self):
        print(self.name, "is treating patients")


class Nurse(Person):
    def assist(self):
        print(self.name, "is assisting patients")


class HeadNurse(Nurse, Doctor):
    def display(self):
        self.assist()
        self.treat_patient()


hn = HeadNurse("NURSE")
hn.display()