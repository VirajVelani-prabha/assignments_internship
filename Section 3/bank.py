
class BankAccount:
    def __init__(self, account_number, holder_name, balance):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = balance

    def display(self):
        print("Account Number:", self.account_number)
        print("Holder Name:", self.holder_name)
        print("Balance:", self.balance)

acc1 = BankAccount(1001, "Rahul", 25000)
acc2 = BankAccount(1002, "Priya", 40000)

print("Account 1 Details")
acc1.display()

print("\nAccount 2 Details")
acc2.display()