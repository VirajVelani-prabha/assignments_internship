<<<<<<< HEAD
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
=======
class Company:
    company_name = "TCS"

    def __init__(self, emp_name):
        self.emp_name = emp_name

    def display(self):
        print("Employee Name:", self.emp_name)
        print("Company Name:", Company.company_name)

e1 = Company("Rahul")
e2 = Company("Priya")

e1.display()
print()
e2.display()
>>>>>>> 311fd1035d158aae48cdc680a3b52c4edde99c26
