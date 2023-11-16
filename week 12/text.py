import unittest

class MyTestCase(unittest.TestCase):
    def setUp(self):
        # Set up any fixtures needed for the tests
        self.data = [1, 2, 3, 4, 5]

    def test_sum(self):
        result = sum(self.data)
        self.assertEqual(result, 15, "Sum is incorrect")

    def test_length(self):
        length = len(self.data)
        self.assertEqual(length, 5, "Length is incorrect")

if __name__ == '__main__':
    unittest.main()
