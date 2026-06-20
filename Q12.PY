<<<<<<< HEAD
class Animal:
    def make_sound(self):
        print("Animal makes sound")


class Dog(Animal):
    def make_sound(self):
        print("Dog barks")


class Cat(Animal):
    def make_sound(self):
        print("Cat meows")


class Lion(Animal):
    def make_sound(self):
        print("Lion roars")


animals = [Dog(), Cat(), Lion()]

for a in animals:
    a.make_sound()
=======
class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(c):
        print("Fahrenheit:", (c * 9/5) + 32)

TemperatureConverter.celsius_to_fahrenheit(25)
>>>>>>> 311fd1035d158aae48cdc680a3b52c4edde99c26
