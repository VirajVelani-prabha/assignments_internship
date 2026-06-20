class Employee:
    def __init__(self, emp_id, emp_name, department):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.department = department

    def display(self):
        print("Employee ID:", self.emp_id)
        print("Employee Name:", self.emp_name)
        print("Department:", self.department)

e1 = Employee(101, "Rahul", "IT")

e1.display()