class Character:

    def __init__(self, health=10, power=10, shield=10):
        self.health = health
        self.power = power
        self.shield = shield

    def attack(self, other):
        other.health = other.health - (self.power - other.shield)


player = Character(power=100)
enemy = Character(power=2, shield=0)

print(enemy.health)
player.attack(enemy)
print(enemy.health)
