import unittest


def square(x):
    return x * x


class TestSquareFunction(unittest.TestCase):

    def __init__(self):
        self.number = 4

    def test_square_positive(self):
        self.assertEqual(square(self.number), 4)

    def test_square_negative(self):
        self.assertEqual(square(-3), 9)

    def test_square_zero(self):
        self.assertEqual(square(0), 0)

if __name__ == "__main__":
    unittest.main()
