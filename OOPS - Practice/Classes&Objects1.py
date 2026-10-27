#Step 1: Classes and Objects 🏗️

class Monster:      #Blueprint (Class)

    def __init__(self, name, color):        # This __init__ function sets up the monster when it's created
        self.name = name        #Attribute 1
        self.color = color      #Attribute 2


boss_monster = Monster("Dracula", "Black")      # The Actual Thing (Object)

# print(boss_monster.name)
# print(boss_monster.color)

#--------------------------------


class Player:

    def __init__(self, name, score):
        self.name = name
        self.score = score

this_player = Player("Iqbal", 10)
print(this_player.name)