# The Parent Class
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_details(self):
        return f"{self.name} makes ${self.salary}"

class Developer(Employee):
    def __init__(self, name, salary, programming_langugage):
        super().__init__(name, salary)
        self.pl = programming_langugage

class Manager(Employee):
    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)
        self.team_size = team_size

#List of employees
roster = [Developer("Alice", 80000, "Python"), 
          Manager("Bob", 120000, 5)
          ]

for emp in roster:

    if isinstance(emp, Developer):
        print(f"{emp.name} writes code in {emp.pl} language")
    elif isinstance(emp, Manager):
        print(f"{emp.name} manages a team of {emp.team_size} people")  