import random
from abc import ABC, abstractmethod


class Character(ABC):
    count = 0

    def __init__(self, name, health, power):
        self.name = name
        self.__health = health
        self.max_health = health
        self.power = power
        self.potions = 2

        Character.count += 1

    # Encapsulation
    def get_health(self):
        return self.__health

    def take_damage(self, amount):
        self.__health -= amount

        if self.__health < 0:
            self.__health = 0

    def heal(self, amount):
        self.__health += amount

        if self.__health > self.max_health:
            self.__health = self.max_health

    def is_alive(self):
        return self.__health > 0

    def use_potion(self):
        if self.potions == 0:
            return "No potions left!"

        self.potions -= 1
        self.heal(35)

        return (
            f"{self.name} drinks a potion and recovers "
            f"35 HP. ({self.potions} left)"
        )

    def show_status(self):
        return f"{self.name}: HP {self.__health}/{self.max_health}"

    def can_use_special(self):
        return True

    @abstractmethod
    def attack(self, target):
        pass

    @abstractmethod
    def special_move(self, target):
        pass

    @classmethod
    def total_characters(cls):
        return cls.count
