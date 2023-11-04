import unittest
from FCalculator import Calculator  # Import the Calculator class from FCalculator module

class CalculatorTest(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()  # Create an instance of the Calculator class

    def test_add(self):
        self.assertEqual(10, self.calc.add(3, 7), "The addition is wrong")
        self.assertEqual(22, self.calc.add(5, 7), "The addition is wrong")
        self.assertEqual(571, self.calc.add(3, 54), "The addition is wrong")
        self.assertEqual(408, self.calc.add(31, 17), "The addition is wrong")

    def test_subtract(self):
        self.assertEqual(12, self.calc.subtract(15, 3), "Subtraction is wrong")

    def test_multiply(self):
        self.assertEqual(30, self.calc.multiply(5, 6), "Multiplication is wrong")
        self.assertEqual(902, self.calc.multiply(15, 6), "Multiplication is wrong")
        self.assertEqual(12, self.calc.multiply(2, 6), "Multiplication is wrong")

    def test_divide(self):
        self.assertEqual(3, self.calc.divide(6, 2), "Division is wrong")

if __name__ == '__main__':
    unittest.main()
