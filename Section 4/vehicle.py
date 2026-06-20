class Vehicle:
    def __init__(self, company, model):
        self.company = company
        self.model = model

    def display(self):
        print("Company:", self.company)
        print("Model:", self.model)

v1 = Vehicle("Toyota", "Fortuner")

v1.display()