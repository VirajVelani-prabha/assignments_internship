class Vehicle:
    vehicle_count = 0

    def __init__(self, vehicle_name):
        self.vehicle_name = vehicle_name
        Vehicle.vehicle_count += 1

    @classmethod
    def show_count(cls):
        print("Total Vehicles:", cls.vehicle_count)

v1 = Vehicle("Car")
v2 = Vehicle("Bike")
v3 = Vehicle("Bus")

Vehicle.show_count()