class Bird:

    def fly(self):
        pass

class Sparrow(Bird):

    def fly(self):
        print("Sparrow flies low")

class Eagle(Bird):

    def fly(self):
        print("Eagle flies high")

birds = [Sparrow(), Eagle()]

for bird in birds:
    bird.fly()