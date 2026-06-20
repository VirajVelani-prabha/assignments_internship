<<<<<<< HEAD
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
=======
class Mobile:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def display(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Price:", self.price)

m1 = Mobile("Samsung", "Galaxy S24", 80000)

m1.display()
>>>>>>> 311fd1035d158aae48cdc680a3b52c4edde99c26
