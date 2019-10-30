import unittest
from Calculator import Calculator
from CsvReader import CsvReader
from pprint import pprint


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.calculator = (Calculator)


    def test_instantiate_calculator(self):
        calculator = Calculator()
        self.assertIsInstance(calculator, Calculator)


    def test_results_property_calculator(self):
        calculator  = Calculator()
        self.assertEqual(calculator.result, 4)
        test_data = CsvReader('/src/Unit_Test_Addition.csv').data
        pprint(test_data)

    def test_add_method_calculator(self):
        calculator = Calculator()
        self.assertEqual(calculator.add(2, 2), 4)
        self.assertEqual(calculator.result, 4)
        test_data = CsvReader('/src/Unit_Test_Subtraction.csv').data
        pprint(test_data)

    def test_subtract_method_calculator(self):
        calculator = Calculator()
        self.assertEqual(calculator.subtract(2, 2), 0)
        self.assertEqual(calculator.result, 0)

    def test_multiplication_method_calculator(self):
            calculator = Calculator()
            self.assertEqual(calculator.multipy(2, 2), 4)
            self.assertEqual(calculator.result, 4)

    def test_division_method_calculator(self):
        calculator = Calculator()
        self.assertEqual(calculator.divide(2, 2), 1)
        self.assertEqual(calculator.result, 1)

    def test_squared_method_calculator(self):
        calculator = Calculator()
        self.assertEqual(calculator.squared(3, ), 9)
        self.assertEqual(calculator.result, 9)

    def test_sqrt_method_calculator(self):
        calculator = Calculator()
        self.assertEqual(calculator.sqrt(9, ), 3)
        self.assertEqual(calculator.result, 3)


if __name__ == '__main__':
    unittest.main()
