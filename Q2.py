class Vehicle:
    def __init__(self, brand):
        self.brand = brand


class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model


class Bike(Vehicle):
    def __init__(self, brand, bike_type):
        super().__init__(brand)
        self.bike_type = bike_type


class ElectricCar(Car):
    def __init__(self, brand, model, battery_capacity):
        super().__init__(brand, model)
        self.battery_capacity = battery_capacity


class SportsElectricCar(ElectricCar):
    def __init__(self, brand, model, battery_capacity, top_speed):
        super().__init__(brand, model, battery_capacity)
        self.top_speed = top_speed

    def display(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Battery Capacity:", self.battery_capacity, "kWh")
        print("Top Speed:", self.top_speed, "km/h")


sec = SportsElectricCar("Tesla", "Roadster", 200, 400)
sec.display()