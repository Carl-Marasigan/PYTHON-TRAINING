import unittest

def add(a, b):
    return a + b

def square(x):
    return x * x

def multiply(a, b):
    return a * b

def calculate_expression(x, y):
    return add(square(x), multiply(y, 2))

class TestCalculateExpression(unittest.TestCase):

    def test_calculate_expression(self):
        self.assertEqual(calculate_expression(2, 3), 10)  # 2^2 + 3*2 = 4 + 6
        self.assertEqual(calculate_expression(0, 5), 10)   # 0^2 + 5*2 = 0 + 10
        self.assertEqual(calculate_expression(1, 1), 3)    # 1^2 + 1*2 = 1 + 2
        self.assertEqual(calculate_expression(-1, 2), 5)   # (-1)^2 + 2*2 = 1 + 4

if __name__ == "__main__":
    unittest.main()
