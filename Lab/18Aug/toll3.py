#Program with report and count of cars and amount collected. Also, it keeps track of the number of times a car has not paid the toll. If a car has not paid 5 times, it cannot pass the toll.

class Toll:
    def __init__(self):
        self._carCount = 0
        self._amount = 0
        self.collectionOfReg = {}
        self._collectionOfVehicles = {}

    def amount(self, vehicle_type):
        if vehicle_type.lower() == "car":
            return 100
        else:
            return 500

    def carpass(self, isPaid, registrationNumber, vehicle_type):
        toll_fee = self.amount(vehicle_type)

        if isPaid == True:
            self._carCount += 1
            self._amount += toll_fee

            if registrationNumber in self._collectionOfVehicles:
                self._collectionOfVehicles[registrationNumber][1] += toll_fee
            else:
                self._collectionOfVehicles[registrationNumber] = [vehicle_type, toll_fee]

            print(f"Vehicle {registrationNumber} has passed")
            print(f"Vehicle Type: {vehicle_type}")
            print(f"Toll Paid: Rs.{toll_fee}")
            print(f"Total Amount Collected: Rs.{self._amount}")

        else:
            if registrationNumber in self.collectionOfReg:
                self.collectionOfReg[registrationNumber] += 1
            else:
                self.collectionOfReg[registrationNumber] = 1

            times = self.collectionOfReg[registrationNumber]

            if times >= 5:
                print(f"Vehicle {registrationNumber} has not paid 5 times so CANNOT PASS!!!")
            else:
                print(f"Vehicle {registrationNumber} has not paid. Warning {times}/5")
            print(f"Vehicle Type: {vehicle_type}")
            print(f"Toll Due: Rs.{toll_fee}")

    def showReport(self):
        print("\n--- Toll ---")
        print(f"Total passed vehicles: {self._carCount}")
        print(f"Total amount collected: Rs.{self._amount}")
        print(f"Unpaid count per vehicle: {self.collectionOfReg}")
        print(f"Vehicle payment record: {self._collectionOfVehicles}")

toll = Toll()

while True:
    choice = input("\nEnter 1 to pass the toll or 2 to exit: ")

    if choice == "1":
        typeInput = input("Enter vehicle type: Car/Heavy Vehicle: ")
        paidInput = input("Has the vehicle paid the toll? True/False: ")
        registrationNumber = input("Enter the registration number: ")

        isPaid = True if paidInput.lower() == "true" else False

        toll.carpass(isPaid, registrationNumber, typeInput)

    elif choice == "2":
        toll.showReport()
        print("Exiting toll")
        break
    else:
        print("Invalid choice. Enter 1 or 2")