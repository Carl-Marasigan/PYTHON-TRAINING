class ExampleClass:

    def __init__(self, name, age):
        self.name = name
        self.age = age

        print(f"Object is name as {name}, with age {age}. ")

example = ExampleClass("Carl", 26)

print(f"Name of example instance is:{example.name}")
print(f"Age of example instance is:{example.age}")




