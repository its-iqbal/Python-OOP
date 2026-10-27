#Step 2: Methods (The Actions) 🏃‍♂️

class Robot:

    def __init__(self, name, battery_level):
        self.name = name
        self.battery_level = battery_level

    #This is method
    def charge(self):
        self.battery_level = 100
        print(f"{self.name} is now fully charged!")

my_robot = Robot("Robo", 50)    #Create the object

# my_robot.charge()  #Calling the method
# print(my_robot.battery_level)  #Check the battery level after charging

#---------------------------------------


class Player:

    def __init__(self, name, score):
        self.name = name
        self.score = score

    #Method
    def score_point(self):
        self.score += 1
        print(f"{self.name} scored a point! Total score: {self.score}")

this_player = Player("Iqbal", 10)
this_player.score_point()  #Calling the method
print(this_player.score)  #Check the score after scoring a point