
class Mobile:
    def __init__(self, company, model, storage):
        self.company = company
        self.model = model
        self.storage = storage


mobile1 = Mobile("Samsung", "Galaxy S24", "128 GB")
mobile2 = Mobile("Apple", "iPhone 15", "256 GB")
mobile3 = Mobile("OnePlus", "12R", "128 GB")

print("Mobile 1")
print("Company:", mobile1.company)
print("Model:", mobile1.model)
print("Storage:", mobile1.storage)

print("\nMobile 2")
print("Company:", mobile2.company)
print("Model:", mobile2.model)
print("Storage:", mobile2.storage)

print("\nMobile 3")
print("Company:", mobile3.company)
print("Model:", mobile3.model)
print("Storage:", mobile3.storage)