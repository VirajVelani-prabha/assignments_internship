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