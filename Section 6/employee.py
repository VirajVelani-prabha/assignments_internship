class Employee:
    def __init__(self, emp_name, monthly_salary):
        self.emp_name = emp_name
        self.monthly_salary = monthly_salary

    def annual_salary(self):
        yearly_salary = self.monthly_salary * 12
        print("Employee Name:", self.emp_name)
        print("Annual Salary:", yearly_salary)

e1 = Employee("Rahul", 50000)

e1.annual_salary()