<<<<<<< HEAD
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
=======
class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)
        print("Balance:", self.balance)

    def withdraw(self, amount):
        self.balance -= amount
        print("Withdrawn:", amount)
        print("Balance:", self.balance)

acc = BankAccount(10000)

acc.deposit(5000)
acc.withdraw(2000)
>>>>>>> 311fd1035d158aae48cdc680a3b52c4edde99c26
