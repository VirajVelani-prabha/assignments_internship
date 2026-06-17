class Animal:
    def __init__(self, animal_name, color):
        self.animal_name = animal_name
        self.color = color

    def display(self):
        print("Animal Name:", self.animal_name)
        print("Color:", self.color)

a1 = Animal("Tiger", "Orange")

a1.display()