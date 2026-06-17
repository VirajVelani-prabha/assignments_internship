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