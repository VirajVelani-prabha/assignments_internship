class Employee:
    def __init__(self, name):
        self.name = name


class Developer(Employee):
    def code(self):
        print(self.name, "is writing code")


class Manager(Employee):
    def manage_team(self):
        print(self.name, "is managing the team")


class TechLead(Developer, Manager):
    def display(self):
        self.code()
        self.manage_team()


tl = TechLead("Viraj")
tl.display()