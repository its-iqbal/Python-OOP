import random
from characters.character import Character


class Enemy(Character):
    def attack(self, target):
        damage = random.randint(self.power - 3, self.power + 3)
        target.take_damage(damage)

        return (
            f"{self.name} attacks {target.name} "
            f"for {damage} damage."
        )

    def special_move(self, target):
        damage = int(self.power * 1.5)
        target.take_damage(damage)

        return (
            f"{self.name} makes a wild swing at {target.name} "
            f"for {damage} damage!"
        )

    def take_turn(self, target):
        if random.randint(1, 4) == 1:
            return self.special_move(target)

        return self.attack(target)


class Dragon(Enemy):
    def special_move(self, target):
        damage = self.power * 2
        target.take_damage(damage)

        return (
            f"The Dragon breathes FIRE on {target.name} "
            f"for {damage} damage!"
        )
