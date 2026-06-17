<<<<<<< HEAD
class Employee:
    def role(self):
        print("Employee")


class Developer(Employee):
    def role(self):
        print("Developer")


class Tester(Employee):
    def role(self):
        print("Tester")


class Manager(Employee):
    def role(self):
        print("Manager")


employees = [Developer(), Tester(), Manager()]

for e in employees:
    e.role()
=======
class Utility:
    @staticmethod
    def check_even_odd(num):
        if num % 2 == 0:
            print("Even Number")
        else:
            print("Odd Number")

Utility.check_even_odd(7)
>>>>>>> 311fd1035d158aae48cdc680a3b52c4edde99c26
