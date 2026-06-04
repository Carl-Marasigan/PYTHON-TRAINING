class Cat:
    def __init__(self, name):
        self.name = name

    def meow(self, target=None):
        """Add functionality here"""

    def scratch(self, scratched):
        """Add functionality here"""

whiskers = Cat("Whiskers")
tom = Cat("Tom")

whiskers.meow(tom)
whiskers.meow()