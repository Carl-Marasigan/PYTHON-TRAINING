class Number:
    def __init__(self, value):
        self.value = value

    def add(self, other):
        new_value = self.value + other.value
        return Number(new_value)

num1 = Number(2)
num2 = Number(5)
sum = num1.add(num2)

print(f"Sum of num1 and num2 is {sum.value}")




