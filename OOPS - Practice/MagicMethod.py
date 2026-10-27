class Pet:
    def __init__(self, name, animal_type):
        self.name = name
        self.animal_type = animal_type
        
    # Python automatically calls this when we print the object!
    def __str__(self):
        return f"Name is {self.name} the {self.animal_type}"

my_pet = Pet("Garfield", "Cat")

# Instead of a weird memory address, we get our beautiful string!
# print(my_pet) # Output: Name is Garfield the Cat

#--------------------------------

class Player:
    def __init__(self, name, score):
        self.name = name
        self.__score = score
        
    def score_point(self):
        self.__score += 1
        print(f"{self.name} scored a point! Total score: {self.__score}")

    def see_score(self):
        return f"{self.name}'s score: {self.__score}"

    # Add your __str__ method right here!
    def __str__(self):
        return f"Player: {self.name} (Score: {self.__score})"

# Testing the magic method
this_player = Player("Iqbal", 10)

# Instead of a memory address, this should now print your beautiful string!
# print(this_player)


#--------------------------------

class Player:
    def __init__(self, name, score):
        self.name = name
        self.__score = score
        
    def __str__(self):
        return f"Player: {self.name} (Score: {self.__score})"

    # Add your __gt__ method right here!
    def __gt__(self,other):
        return self.__score > other.__score

# Testing the magic method
player1 = Player("Iqbal", 15)
player2 = Player("Babar", 20)

# Python now knows exactly how to compare these two complex objects!
if player1 > player2:
    print(f"{player1.name} is winning!")
else:
    print(f"{player2.name} is winning or tied!")