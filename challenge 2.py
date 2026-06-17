class Employee:
    employee_count = 0

    def __init__(self, emp_id, emp_name, salary):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.salary = salary
        Employee.employee_count += 1

    def display_employee(self):
        print("Employee ID:", self.emp_id)
        print("Employee Name:", self.emp_name)
        print("Salary:", self.salary)

    @classmethod
    def show_total_employees(cls):
        print("Total Employees:", cls.employee_count)

e1 = Employee(101, "Rahul", 50000)
e2 = Employee(102, "Priya", 60000)
e3 = Employee(103, "Amit", 55000)

e1.display_employee()
print()

e2.display_employee()
print()

e3.display_employee()
print()

Employee.show_total_employees()