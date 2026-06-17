

class Animal:
    def __init__(self, name):
        self.name = name


class Dog(Animal):
    def sound(self):
        print("Dog barks")


class Cat(Animal):
    def sound(self):
        print("Cat meows")


class Cow(Animal):
    def sound(self):
        print("Cow moos")


d = Dog("SHERU")
c = Cat("MITHI")
w = Cow("RANI")

d.sound()
c.sound()
w.sound()