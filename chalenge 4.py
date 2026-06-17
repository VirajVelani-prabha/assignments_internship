class Mobile:
    discount_percentage = 10

    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def display_mobile(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Price:", self.price)
        print("Discount:", Mobile.discount_percentage, "%")

    def calculate_discount_price(self):
        discount_price = self.price - (self.price * Mobile.discount_percentage / 100)
        print("Price After Discount:", discount_price)

    @classmethod
    def change_discount(cls, new_discount):
        cls.discount_percentage = new_discount

m1 = Mobile("Samsung", "Galaxy S24", 80000)
m2 = Mobile("Apple", "iPhone 15", 70000)

m1.display_mobile()
m1.calculate_discount_price()

print()

m2.display_mobile()
m2.calculate_discount_price()

Mobile.change_discount(15)

print("\nAfter Changing Discount Percentage:")

m1.display_mobile()
m1.calculate_discount_price()

print()

m2.display_mobile()
m2.calculate_discount_price()