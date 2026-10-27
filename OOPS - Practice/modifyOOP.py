# PROCEDURAL CODE TO BE REFACTORED 
# player1 = {"name": "Ronaldo", "energy": 100} 
# player2 = {"name": "Messi", "energy": 100} 
# def pass_ball(passer, receiver): 
#     print(passer["name"] + " passes the ball to " + receiver["name"]) 
#     passer["energy"] -= 5 
# # Drill actions 
# pass_ball(player1, player2) 
# pass_ball(player2, player1) 
# pass_ball(player1, player2) 
# print("Ronaldo Energy:", player1["energy"]) 
# print("Messi Energy:", player2["energy"]) 

# class Player:

#     def __init__(self, name):
#         self.name = name
#         self.energy = 100

#     def pass_ball_to(self, target_player):
#         print(f"{self.name} Passed ball to {target_player.name}")
#         self.energy -= 5

# player1 = Player("Ronaldo")
# player2 = Player("Messi")

# player1.pass_ball_to(player2)
# player2.pass_ball_to(player1)
# player1.pass_ball_to(player2)

# print(f"Ronaldo Energy: {player1.energy}")
# print(f"Messi Energy: {player2.energy}")


#--------------------------------------------------

# student1 = {"name": "Ali", "marks": []}
# student2 = {"name": "Sara", "marks": []}

# def add_mark(student, mark):
#     student["marks"].append(mark)

# def average(student):
#     return sum(student["marks"]) / len(student["marks"]) if student["marks"] else 0

# add_mark(student1, 85)
# add_mark(student1, 90)
# add_mark(student2, 70)
# print(student1["name"], average(student1))
# print(student2["name"], average(student2))

class Student:
    def __init__(self, name, marks=None):
        self.name = name
        if marks is None:
            self.marks = []
        else:
            self.marks = marks

    def add_marks(self, marks):
        self.marks.append(marks)

    def average(self):
        total_marks = 0
        for mark in self.marks:
            total_marks += mark
        return total_marks/len(self.marks)

std1 = Student("Ali", [100, 100, 100])
std2 = Student("Sara", [90, 80, 100])

res1 = std1.average()
print(res1)

std2.add_marks(40)
res2 = std2.average()
print(res2)

std3 = Student("Hadi")
std3.add_marks(20)
print(std3.average())