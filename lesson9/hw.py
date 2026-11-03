class GameCharacter:
    def __init__(self, name, damage, health):
        self.name = name
        self.damage = damage
        self.health = health

    def attack(self):
        print(f"{self.name} attacked {self.damage} damage.")

    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0
        print(f"{self.name} takes {damage} damage.")
        print(f"remaining health: {self.health}")

game_character = GameCharacter("John", 100, 100)

game_character.attack()
print(game_character.health)
game_character.take_damage(100)
