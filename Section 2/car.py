class car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model

car1 = car("BMW","M7")
car2 = car("MERCEDES","G=CLASS")

print("car 1=")
print("brand=",car1.brand)
print("model=",car1.model)

print("\ncar 2")
print("brand=",car2.brand)
print("model=",car2.model)