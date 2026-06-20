from abc import ABC, abstractmethod

# Abstract Class
class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass

# Child Class
class Car(Vehicle):

    def start(self):
        print("Car is starting...")

# Create object and call method
c = Car()
c.start()