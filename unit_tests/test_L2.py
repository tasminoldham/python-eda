import unittest
from calculator import Calculator

class TestCalculations(unittest.TestCase):

    def setUp(self):
        self.operator = Calculator(a=8, b=2)

    def test_sum(self):
        self.assertEqual(self.operator.get_sum(), 10, 'this sum is wrong')

    def test_product(self):
        self.assertEqual(self.operator.get_product(), 16,'the sum is wrong..not really')

    def tearDown(self):
        print('all tests ran. bye')

if __name__ == '__main__':
    unittest.main()