import random
from characters.character import Character


class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, 100, 11)
        self.rage = 0

    def attack(self, target):
        damage = random.randint(self.power - 3, self.power + 3)
        target.take_damage(damage)
        self.rage += 10

        return (
            f"{self.name} slashes {target.name} for "
            f"{damage} damage. (+10 rage)"
        )

    def can_use_special(self):
        return self.rage >= 30

    def special_move(self, target):
        self.rage -= 30
        damage = self.power * 2
        target.take_damage(damage)

        return (
            f"{self.name} uses POWER STRIKE on "
            f"{target.name} for {damage} damage!"
        )


class Mage(Character):
    def __init__(self, name):
        super().__init__(name, 90, 11)
        self.mana = 50
        self.max_mana = 50

    def restore_mana(self, amount):
        self.mana += amount

        if self.mana > self.max_mana:
            self.mana = self.max_mana

    def attack(self, target):
        damage = random.randint(self.power - 3, self.power + 3)
        target.take_damage(damage)
        self.restore_mana(8)

        return (
            f"{self.name} hits {target.name} with a magic bolt "
            f"for {damage} damage. (+8 mana)"
        )

    def can_use_special(self):
        return self.mana >= 20

    def special_move(self, target):
        self.mana -= 20
        damage = self.power * 2 + 5
        target.take_damage(damage)

        return (
            f"{self.name} casts FIREBALL on {target.name} "
            f"for {damage} damage!"
        )


class Paladin(Warrior, Mage):
    def __init__(self, name):
        Character.__init__(self, name, 100, 11)

        self.rage = 0
        self.mana = 30
        self.max_mana = 30

    def attack(self, target):
        message = super().attack(target)
        self.restore_mana(3)

        return message + " (+3 mana)"

    def can_use_special(self):
        return self.mana >= 20

    def special_move(self, target):
        self.mana -= 20
        damage = self.power * 2
        target.take_damage(damage)
        self.heal(15)

        return (
            f"{self.name} uses HOLY SMITE on {target.name} "
            f"for {damage} damage and heals 15 HP!"
        )
