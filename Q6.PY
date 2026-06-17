class Employee:
    def __init__(self, name):
        self.name = name

    def work(self):
        print("Employee is working")


class Developer(Employee):
    def work(self):
        print(self.name, "is developing software")


class Tester(Employee):
    def work(self):
        print(self.name, "is testing software")


class Designer(Employee):
    def work(self):
        print(self.name, "is designing UI/UX")


d = Developer("Rahul")
t = Tester("Priya")
de = Designer("Amit")

d.work()
t.work()
de.work()