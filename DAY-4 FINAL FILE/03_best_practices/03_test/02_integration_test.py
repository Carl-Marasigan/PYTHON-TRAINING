"""
Integration Test:

Testing if different components work well when used together
"""

def add(a, b):
    return a + b

def square(x):
    return x * x

def multiply(a, b):
    return a * b

# x^2 + 2y
def calculate_expression(x, y):
    return add(square(x), multiply(y, 2))

def test_calculate_expression():
    assert calculate_expression(2, 3) == 10   # 2^2 + 3*2 = 4 + 6
    assert calculate_expression(0, 5) == 10    # 0^2 + 5*2 = 0 + 10
    print("All integration tests passed!")

test_calculate_expression()
