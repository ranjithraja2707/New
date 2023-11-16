import unittest

class MyTestCase(unittest.TestCase):
    def test_addition(self):
        result = 2 + 2
        self.assertEqual(result, 4, "Addition is incorrect")

    def test_boolean(self):
        value = True
        self.assertTrue(value, "Value should be True")

if __name__ == '__main__':
    unittest.main()
