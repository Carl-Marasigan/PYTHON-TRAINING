"""
Unit Test:

Testing individual components or functions in isolation from other parts
to ensure the functions work as intended.
"""

def square(x):
    return x * x

def test_square():
    assert square(2) == 4
    assert square(-3) == 9
    assert square(0) == 0
    print("All unit tests passed!")

test_square()