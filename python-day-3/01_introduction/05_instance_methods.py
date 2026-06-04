class ExampleClass:

    def __init__(self, value1, value2):
        self.value1 = value1
        self.value2 = value2

        print(f"Object created with {value1}, {value2}")

    def sum(self):
        return self.value1 + self.value2
    def multiply(self):
        return self.value1*self.value2

instance_methods = ExampleClass(12345, 23456)
print(instance_methods.sum())
print(instance_methods.multiply())
print(f"Sum of example instance is: {instance_methods.sum()}")
print(f"Multiplication of example instance is:.{instance_methods.multiply()}")

