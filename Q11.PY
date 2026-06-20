<<<<<<< HEAD
class Notification:
    def send(self):
        print("Sending notification")


class EmailNotification(Notification):
    def send(self):
        print("Sending Email Notification")


class SMSNotification(Notification):
    def send(self):
        print("Sending SMS Notification")


class PushNotification(Notification):
    def send(self):
        print("Sending Push Notification")


notifications = [
    EmailNotification(),
    SMSNotification(),
    PushNotification()
]

for n in notifications:
    n.send()
=======
class Calculator:
    @staticmethod
    def add(a, b):
        print("Addition:", a + b)

    @staticmethod
    def subtract(a, b):
        print("Subtraction:", a - b)

    @staticmethod
    def multiply(a, b):
        print("Multiplication:", a * b)

    @staticmethod
    def divide(a, b):
        print("Division:", a / b)

Calculator.add(10, 5)
Calculator.subtract(10, 5)
Calculator.multiply(10, 5)
Calculator.divide(10, 5)
>>>>>>> 311fd1035d158aae48cdc680a3b52c4edde99c26
