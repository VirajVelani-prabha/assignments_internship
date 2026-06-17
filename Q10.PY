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