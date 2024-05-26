# my_module.py
class Calculator:
    def __init__(self):
        pass

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero!")
        return a / b

def square(x):
    return x * x

def cube(x):
    return x * x * x

class Average:
    def __init__(self, numbers):
        self.numbers = numbers

    def calculate(self):
        if not self.numbers:
            return 0
        return sum(self.numbers) / len(self.numbers)

class ComplexNumber:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, other):
        real = self.real + other.real
        imaginary = self.imaginary + other.imaginary
        return ComplexNumber(real, imaginary)

    def __sub__(self, other):
        real = self.real - other.real
        imaginary = self.imaginary - other.imaginary
        return ComplexNumber(real, imaginary)

    def __mul__(self, other):
        real = self.real * other.real - self.imaginary * other.imaginary
        imaginary = self.real * other.imaginary + self.imaginary * other.real
        return ComplexNumber(real, imaginary)

    def __str__(self):
        return f"{self.real} + {self.imaginary}i"
