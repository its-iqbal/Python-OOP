# class Sprinter: 
#     def __init__(self, name): 
#         self.name = name 
#         self.energy = 100 

#     def run_stage(self, miles): 
#         # BUG IS IN THIS METHOD 
#         energy_loss = miles * 2 

#         #There should be self.energy that will change the energy attribute of main constructor, making another variable wont change the main attribute
#         self.energy = self.energy - energy_loss 
#         print(f"{self.name} completed the stage.") 

#     def view_stats(self): 
#         print(f"{self.name}'s current energy: {self.energy}") 

# # Testing the code 
# runner = Sprinter("Bolt") 
# runner.run_stage(15) 
# runner.view_stats() # Expected: 70, but Outputs: 100 

#------------------------------------------------------

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        # "balance" (no self.) creates a LOCAL variable — it only exists inside this
        # method call and disappears afterward. Using "self.balance" instead makes it
        # an INSTANCE variable, which persists on the object and is visible everywhere.
        self.balance = self.balance + amount
        print(f"New balance should be {self.balance}")

    def show_balance(self):
        print(f"{self.owner}'s balance: {self.balance}")

acc = BankAccount("Iqbal", 500)
acc.deposit(200)
acc.show_balance()   # Expected: 700, but prints: 500