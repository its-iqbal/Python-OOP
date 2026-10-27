#Step 3: Inheritance 🧬

#Parent Class
class Monster:      #Blueprint (Class)

    def __init__(self, name):        # This __init__ function sets up the monster when it's created
        self.name = name        #Attribute

    #Method
    def roar(self):
        print("RAWWR!")

# Child Class (Inherits from Monster by putting it in parentheses)
class flyingMonster(Monster):

    #New Method
    def fly(self):
        print(f"{self.name} takes to the skies! 🦅")

#Child Object
dragon = flyingMonster("Smaug")

# dragon.roar()  #Calling the method from the parent class
# dragon.fly()   #Calling the method from the child class


#--------------------------------


class Player:

    def __init__(self, name, score):
        self.name = name
        self.score = score

    #Method
    def score_point(self):
        self.score += 1
        print(f"{self.name} scored a point! Total score: {self.score}")

class PremiumPlayer(Player):

    #Method
    def bonus_point(self):
        self.score += 2
        print(f"{self.name} scored a bonus point! Total score: {self.score}")

Prem_Player = PremiumPlayer("Babar", 50)

Prem_Player.score_point()  #Calling the method from the parent class
Prem_Player.bonus_point()  #Calling the method from the child class