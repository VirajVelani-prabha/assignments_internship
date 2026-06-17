class Employee:
    def work(self):
        print("Employee is working")


class Developer(Employee):
    def work(self):
        print("Developer is writing code")


class Tester(Employee):
    def work(self):
        print("Tester is testing software")


class Designer(Employee):
    def work(self):
        print("Designer is creating UI designs")


d = Developer()
t = Tester()
de = Designer()

d.work()
t.work()
de.work()