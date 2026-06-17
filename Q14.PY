<<<<<<< HEAD
class Vehicle:
    def start(self):
        print("Vehicle started")


class Car(Vehicle):
    def start(self):
        print("Car started")


class Bike(Vehicle):
    def start(self):
        print("Bike started")


class Bus(Vehicle):
    def start(self):
        print("Bus started")


vehicles = [Car(), Bike(), Bus()]

for v in vehicles:
    v.start()
=======
class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def display(self):
        print("Name:", self.name)

s = Student("Rahul")
s.display()
>>>>>>> 311fd1035d158aae48cdc680a3b52c4edde99c26
