from pathlib import Path

class Character:
    def __init__(self, name, level, hp, attack):
        self.name = name
        self.level = level
        self.hp = hp
        self.attack_power = attack

    def display(self):
        print(f"Name: {self.name}")
        print(f"Level: {self.level}")
        print(f"HP: {self.hp}")
        print(f"Attack: {self.attack_power}")

    def take_damage(self, damage):
        print(f"{self.name} lost {damage} HP.")
        self.hp -= damage

        if self.hp < 0:
            self.hp = 0

    def level_up(self):
        self.level += 1
        self.hp += 100
        self.attack_power += 20

        print(f"{self.name} leveled up!")

    def attack_target(self, target):
        print(f"{self.name} attacks {target.name}!")

        target.take_damage(self.attack_power)

class Warrior(Character):
    def __init__(self, name, level, hp, attack, armor):
        super().__init__(name, level, hp, attack)
        self.armor = armor

    def display(self):
        print(f"Warrior: {self.name}")
        print(f"Level: {self.level}")
        print(f"HP: {self.hp}")
        print(f"Attack: {self.attack_power}")
        print(f"Armor: {self.armor}")

class Mage(Character):
    def __init__(self, name, level, hp, attack, mana):
        super().__init__(name, level, hp, attack)
        self.mana = mana

    def display(self):
        print(f"Mage: {self.name}")
        print(f"Level: {self.level}")
        print(f"HP: {self.hp}")
        print(f"Attack: {self.attack_power}")
        print(f"Mana: {self.mana}")

class GameManager:
    def __init__(self):
        self.characters = []

    def add_character(self, character):
        self.characters.append(character)

    def show_all(self):
        for character in self.characters:
            character.display()
            print("------------")

    def find_character(self, name):
        for character in self.characters:
            if character.name == name:
                return character

        return None

    def remove_character(self, name):
        character = self.find_character(name)

        if character:
            self.characters.remove(character)
            print(f"{name} removed.")
        else:    
            print("Character not found.")

    def make_attack(self, attacker_name, target_name):

        attacker = self.find_character(attacker_name)
        target = self.find_character(target_name)

        if attacker and target:
            attacker.attack_target(target)

        else:
            print("Character not found.")

    def save_game(self, filename):
        path = Path(filename)

        contents = ''

        for character in self.characters:
            if isinstance(character, Warrior):
                contents += (
                    f"Warrior,"
                    f"{character.name},"
                    f"{character.level},"
                    f"{character.hp},"
                    f"{character.attack_power},"
                    f"{character.armor}\n"
                )

            elif isinstance(character, Mage):
                contents += (
                    f"Mage,"
                    f"{character.name},"
                    f"{character.level},"
                    f"{character.hp},"
                    f"{character.attack_power},"
                    f"{character.mana}\n"
                )

        path.write_text(contents, encoding="utf-8")

        print("Game saved.")

    def load_game(self, filename):
        path = Path(filename)

        self.characters = []

        try:
            contents = path.read_text(encoding="utf-8")

        except FileNotFoundError:
            print("File not found.")
            return

        lines = contents.splitlines()

        for line in lines:
            if not line:
                continue

            data = line.split(",")
            character_type = data[0]

            if character_type == "Warrior":
                name = data[1]
                level = int(data[2])
                hp = int(data[3])
                attack = int(data[4])
                armor = int(data[5])

                character = Warrior(name, level, hp, attack, armor)

            elif character_type == "Mage":
                name = data[1]
                level = int(data[2])
                hp = int(data[3])
                attack = int(data[4])
                mana = int(data[5])
                
                character = Mage(name, level, hp, attack, mana)

            else:
                continue

            self.characters.append(character)