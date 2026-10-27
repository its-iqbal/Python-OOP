class Monster:
    # 1. This is a Class Variable! It is shared by ALL monsters.
    total_monsters = 0 

    def __init__(self, name):
        self.name = name # Instance variable (unique to this monster)
        
        # 2. Every time a new monster is created, we increase the shared counter
        Monster.total_monsters += 1 

# The counter starts at 0
# print("Initial monster count: " + str(Monster.total_monsters)) # Output: 0

# Create two monsters
m1 = Monster("Goblin")
m2 = Monster("Dragon")

# The counter is now 2!
# print("Final monster count: " + str(Monster.total_monsters)) # Output: 2

#-------------------------------

class Player:

    total_player = 0  # Class variable to keep track of total players
    def __init__(self, name, score):
        self.name = name
        self.__score = score

        Player.total_player += 1  # Increment the class variable whenever a new player is created

print("Initial player count: " + str(Player.total_player)) # Output: 0

# Testing the magic method
player1 = Player("Iqbal", 15)
player2 = Player("Babar", 20)

print("Final player count: " + str(Player.total_player)) # Output: 2