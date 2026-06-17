class Calculator:
    @staticmethod
    def add(a, b):
        print("Addition:", a + b)

    @staticmethod
    def subtract(a, b):
        print("Subtraction:", a - b)

    @staticmethod
    def multiply(a, b):
        print("Multiplication:", a * b)

    @staticmethod
    def divide(a, b):
        print("Division:", a / b)

Calculator.add(10, 5)
Calculator.subtract(10, 5)
Calculator.multiply(10, 5)
Calculator.divide(10, 5)