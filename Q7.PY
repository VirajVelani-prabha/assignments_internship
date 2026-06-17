class Company:
    company_name = "TCS"

    def __init__(self, emp_name):
        self.emp_name = emp_name

    def display(self):
        print("Employee Name:", self.emp_name)
        print("Company Name:", Company.company_name)

e1 = Company("Rahul")
e2 = Company("Priya")

e1.display()
print()
e2.display()