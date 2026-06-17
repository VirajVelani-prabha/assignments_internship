class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)

    def withdraw(self, amount):
        self.balance -= amount
        print("Withdrawn:", amount)

    def display(self):
        print("Account Holder:", self.account_holder)
        print("Balance:", self.balance)

acc = BankAccount("Rahul", 10000)

acc.deposit(5000)
acc.withdraw(2000)

acc.display()