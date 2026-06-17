<<<<<<< HEAD
class Payment:
    def pay(self):
        print("Processing payment")


class CreditCardPayment(Payment):
    def pay(self):
        print("Payment made using Credit Card")


class UPIPayment(Payment):
    def pay(self):
        print("Payment made using UPI")


class NetBankingPayment(Payment):
    def pay(self):
        print("Payment made using Net Banking")


payments = [
    CreditCardPayment(),
    UPIPayment(),
    NetBankingPayment()
]

for p in payments:
    p.pay()
=======
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
>>>>>>> 311fd1035d158aae48cdc680a3b52c4edde99c26
