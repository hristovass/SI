# test_my_module.py
import unittest
from my_module import Calculator, square, cube, Average, ComplexNumber

class TestMyModule(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)
        self.assertEqual(self.calc.add(-1, 1), 0)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(2, 1), 1)
        self.assertEqual(self.calc.subtract(2, 2), 0)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(2, 3), 6)
        self.assertEqual(self.calc.multiply(-2, 3), -6)

    def test_divide(self):
        self.assertEqual(self.calc.divide(6, 2), 3)
        self.assertEqual(self.calc.divide(5, 2), 2.5)
        self.assertRaises(ValueError, self.calc.divide, 6, 0)

    def test_square(self):
        self.assertEqual(square(2), 4)
        self.assertEqual(square(3), 9)

    def test_cube(self):
        self.assertEqual(cube(2), 8)
        self.assertEqual(cube(3), 27)

    def test_average(self):
        numbers = [1, 2, 3, 4, 5]
        avg = Average(numbers)
        self.assertEqual(avg.calculate(), 3)

    def test_complex_addition(self):
        num1 = ComplexNumber(1, 2)
        num2 = ComplexNumber(3, 4)
        result = num1 + num2
        self.assertEqual(str(result), "4 + 6i")

    def test_complex_multiplication(self):
        num1 = ComplexNumber(1, 2)
        num2 = ComplexNumber(3, 4)
        result = num1 * num2
        self.assertEqual(str(result), "-5 + 10i")

if __name__ == '__main__':
    unittest.main()
