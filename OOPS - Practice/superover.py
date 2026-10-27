import random

class Batsman:
    def __init__(self, name):
        self.name = name
        self.__runs_scored = 0
    
    def score_runs(self, runs):
        self.__runs_scored += runs

    @property
    def runs_scored(self):
        #getter method
        return self.__runs_scored

batsman = Batsman("Babar")

for i in range(1, 7, 1):
    runs = random.choice([0, 1, 2, 4, 6])

    batsman.score_runs(runs)
    print(f"{i} ball runs scored: {runs}")

print(f"Total runs scored: {batsman.runs_scored}")
