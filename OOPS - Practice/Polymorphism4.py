#Step 4: Polymorphism (Many Forms)

class Player:

    def __init__(self, name, score):
        self.name = name
        self.score = score

    #Method
    def score_point(self):
        self.score += 1
        print(f"{self.name} scored a point! Total score: {self.score}")

    def celebrate(self):
        print("Yayyyyyy!")

class PremiumPlayer(Player):

    #Method
    def bonus_point(self):
        self.score += 2
        print(f"{self.name} scored a bonus point! Total score: {self.score}")

    def celebrate(self):
        print("Yayyyyyy! I'm a Premium Player! 🎉")

Reg_Player = Player("Iqbal", 10)
Pre_Player = PremiumPlayer("Babar", 50)

Reg_Player.celebrate()  #Calling the method from the parent class
Pre_Player.celebrate()  #Calling the method from the child class