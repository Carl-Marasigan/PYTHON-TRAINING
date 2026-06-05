# Integer Variable
variable1: int = 1
print(variable1)

# List of Integers
variable2: list[int] = [1, 2, 3]
print(variable2)

# Dictionary with String Keys and Integer Values
variable3: dict[str, int] = {"a": 123, "b": 456, "c": 890}
print(variable3)

# Dictionary with String Keys and List of Integers as Values
variable4: dict[str, list[int]] = { "num1": [1, 2, 3], "num2": [4] }
print(variable4)

# Tuple with Two Integers
variable5: tuple[int, int] = (0, 1)
print(variable5)

# List of Tuple with Two Integers
variable6: list[tuple[int, int]] = [(9, 1), (2, 3), (5, 2)]
print(variable6)
