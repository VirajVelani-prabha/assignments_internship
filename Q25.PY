class ATM:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        self.__balance -= amount

    def show_balance(self):
        print("Balance:", self.__balance)

a = ATM(10000)

a.deposit(5000)
a.withdraw(2000)
a.show_balance()