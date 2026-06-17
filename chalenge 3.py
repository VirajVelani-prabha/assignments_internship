class BankAccount:
    bank_name = "State Bank of India"

    def __init__(self, account_number, holder_name, balance):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawn:", amount)
        else:
            print("Insufficient Balance")

    def check_balance(self):
        print("Account Number:", self.account_number)
        print("Holder Name:", self.holder_name)
        print("Bank Name:", BankAccount.bank_name)
        print("Balance:", self.balance)

    @classmethod
    def change_bank_name(cls, new_name):
        cls.bank_name = new_name

acc1 = BankAccount(1001, "Rahul", 50000)
acc2 = BankAccount(1002, "Priya", 30000)

acc1.deposit(5000)
acc1.withdraw(2000)
acc1.check_balance()

print()

acc2.deposit(10000)
acc2.withdraw(5000)
acc2.check_balance()

print("\nChanging Bank Name...")

BankAccount.change_bank_name("Bank of Maharashtra")

acc1.check_balance()
print()
acc2.check_balance()