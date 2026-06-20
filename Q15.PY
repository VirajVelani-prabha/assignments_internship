<<<<<<< HEAD
class Device:
    def operate(self):
        print("Operating device")


class Camera(Device):
    def operate(self):
        print("Taking photos")


class Phone(Device):
    def operate(self):
        print("Making calls")


class SmartPhone(Phone):
    def operate(self):
        print("Calling, Browsing and Taking Photos")


devices = [Camera(), Phone(), SmartPhone()]

for d in devices:
    d.operate()
=======
class Vehicle:
    def __init__(self, company):
        self.company = company

class Bike(Vehicle):
    def __init__(self, company, model):
        super().__init__(company)
        self.model = model

    def display(self):
        print(self.company, self.model)

b = Bike("Honda", "Shine")
b.display()
>>>>>>> 311fd1035d158aae48cdc680a3b52c4edde99c26
