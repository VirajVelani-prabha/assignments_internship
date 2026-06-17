class Employee:
    def __init__(self):
        self.__salary = 0

    def set_salary(self, salary):
        self.__salary = salary

    def get_salary(self):
        return self.__salary

e = Employee()
e.set_salary(60000)
print("Salary:", e.get_salary())