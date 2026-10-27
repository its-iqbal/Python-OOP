#Encapsulation 🛡️

class Character:
    def __init__(self, name):
        self.name = name
        self.__health = 100  # Private attribute (encapsulated)

    def see_health(self):
        return f"{self.name}'s health: {self.__health}"

Char = Character("Aragorn")
# print(Char.__health)    # This will raise an AttributeError
# print(Char.see_health())  # Accessing the private attribute through a public method

#--------------------------------


class Player:

    def __init__(self, name, score):
        self.name = name
        self.__score = score

    #Method
    def score_point(self):
        self.__score += 1
        print(f"{self.name} scored a point! Total score: {self.__score}")

    def see_score(self):
        return f"{self.name}'s score: {self.__score}"

this_player = Player("Iqbal", 10)
print(this_player.see_score())  # Accessing the private attribute through a public method
# print(this_player.__score)  # This will raise an AttributeError