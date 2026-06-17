class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)
        print("Balance:", self.balance)

    def withdraw(self, amount):
        self.balance -= amount
        print("Withdrawn:", amount)
        print("Balance:", self.balance)

acc = BankAccount(10000)

acc.deposit(5000)
acc.withdraw(2000)