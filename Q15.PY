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