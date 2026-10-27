#Simple toll program using List

class Toll:
    def __init__(self):
        self._carCount = 0
        self._amount = 0
        self.collectionOfReg = []

    def carpass(self, isPaid, registrationNumber):
        if isPaid == True:
            self._carCount += 1
            self._amount += 100
            print(f"Car {registrationNumber} has passed.")
            print(f"Total amount: {self._amount}")
        else:
            self.collectionOfReg.append(registrationNumber)
            times = self.collectionOfReg.count(registrationNumber)

            if times >= 2:
                print(f"Car {registrationNumber} has not paid 6 times so cannot pass !!!")
            else:
                print(f"Car {registrationNumber} has not paid. Warning {times}/5")

    def showReport(self):
        print("\n--- Toll Data ---")
        print(f"Total passed cars: {self._carCount}")
        print(f"Total amount: {self._amount}")
        print(f"Unpaid cars: {self.collectionOfReg}")

toll = Toll()

while True:
    choice = input("Enter 1 to pass the toll or 2 to exit: ")

    if choice == "1":
        paidInput = input("Has the car paid the toll? True/False: ")
        registrationNumber = input("Enter the registration number of the car: ")
        isPaid = True if paidInput.lower() == "true" else False
        toll.carpass(isPaid, registrationNumber)

    elif choice == "2":
        toll.showReport()
        break
    else:
        print("Invalid choice. Enter 1 or 2")