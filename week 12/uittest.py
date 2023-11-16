def add_numbers(a, b):
    return a + b
import unittest

class TestAddNumbers(unittest.TestCase):
    def test_add_numbers(self):
        result = add_numbers(2, 3)
        self.assertEqual(result, 5)
        result = add_numbers(-1, 5)
        self.assertEqual(result, 4)
if __name__ == '__main__':
    unittest.main()
