#Abstraction 👻

from abc import ABC, abstractmethod

#Template
class Enemy(ABC):      #Abstract Class

    @abstractmethod
    def attack(self):        #Abstract Method
        pass        # We use 'pass' because there is no actual code here, just the rule!

#Actual Class
class Zombie(Enemy):

    # If we forget to include this attack method, Python will throw an error
    def attack(self):
        print("Zombie attacks with a bite! 🧟‍♂️")

# my_zombie = Zombie()
# my_zombie.attack()  #Calling the method

#--------------------------------

from abc import ABC, abstractmethod

class GameItem(ABC):

    @abstractmethod
    def use(self):
        pass

class HealthPotion(GameItem):

    def use(self):
        print("You drank a potion and gained 20 HP! 🧪")

health = HealthPotion()
health.use()  #Calling the method