# test_mymodule.py
import unittest
from mymodule import factorial

class TestFactorialFunction(unittest.TestCase):

    def test_factorial_of_0(self):
        result = factorial(0)
        self.assertEqual(result, 1)

    def test_factorial_of_5(self):
        result = factorial(5)
        self.assertEqual(result, 120)

    def test_factorial_of_negative_number(self):
        with self.assertRaises(ValueError):
            factorial(-1)

if __name__ == '__main__':
    unittest.main()
