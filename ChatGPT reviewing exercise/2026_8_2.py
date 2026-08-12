import random

class Character:
    def __init__(self, name, hp, attack_power, critical_rate=0.2):
        self.name = name
        self.hp = hp 
        self.attack_power = attack_power
        self.critical_rate = critical_rate

    def attack(self, target):
        if random.random() < self.critical_rate:
            damage = self.attack_power * 2
            print("Critical hit!")
        else:
            damage = self.attack_power

        target.hp -= damage
        
        if target.hp < 0:
            target.hp = 0

        print(f"{self.name} attacks {target.name} for {self.attack_power} damage.")

    def is_alive(self):
        return self.hp > 0


class Game:
    def __init__(self):
        self.characters = []

    def add_character(self, character):
        self.characters.append(character)

    def show_status(self):
        for character in self.characters:
            print(f"{character.name}: HP={character.hp}")

    def battle(self, player, enemy):
        while enemy.is_alive() and player.is_alive():
            player.attack(enemy)
            if not enemy.is_alive():
                break

            enemy.attack(player)

        if player.is_alive():
            print(f"{player.name} is defeated!")
        else:
            print(f"{enemy.name} is defeated!")



knight = Character(
    "Knight",
    100,
    20,
    0.3
)

wolf = Character(
    "Wolf",
    80,
    15,
    0.5
)

game = Game()

game.battle(
    knight,
    wolf
)