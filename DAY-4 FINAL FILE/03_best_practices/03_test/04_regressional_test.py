"""
Regression Test:

Check if changes in the code have not affected existing functionality.
"""

def add(a, b):
    return a + b

def square(x):
    return x * x

def multiply(a, b):
    return a * b

def calculate_expression(x, y):
    return add(square(x), multiply(y, 2))

def test_regression():
    # Test existing functionality
    assert calculate_expression(2, 3) == 10  # 2^2 + 3*2 = 4 + 6
    assert calculate_expression(0, 5) == 10    # 0^2 + 5*2 = 0 + 10

    # New functionality can be added here
    # For example, if you change `calculate_expression` to also accept a third parameter for subtraction:
    """
    def calculate_expression(x, y, z=0):
        return add(square(x), multiply(y, 2)) - z

    # Test the new functionality
    assert calculate_expression(2, 3, 2) == 8  # (2^2 + 3*2) - 2 = 10 - 2 = 8
    """

    print("All regression tests passed!")

test_regression()
