class Dog:

    population = 0
    population_good_boy = 0
    scientific_name = "Canis lupus familiaris"

    def __init__(self,name, good_boy = True):
        self.name = name
        self.gets_treats = good_boy
        Dog.population = Dog.population + 1

    def bark(self):
        print("Bark")

print(Dog.population)
dog1 = Dog("Rocky")

print(Dog.population)
dog2 = Dog("Blitz")

print(Dog.population)
print(dog1.scientific_name)