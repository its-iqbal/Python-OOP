#bank
# Encapsulation
class Account:
    def __init__(self, title, accNo, balance):
        self.title = title
        self.accNo = accNo
        self.__balance = balance
        self.trans_history = []
        self.total_withdrawals = 0.0
        self.total_deposits = 0.0

    
    def show_bal(self):
        return self.__balance

    # Method overloading
    def deposit(self, amount):
        self.__balance += amount
        self.total_deposits += amount
        self.trans_history.append("Deposit: +" + str(amount))
        return "Deposit successful. New balance: " + str(self.__balance)

    def withdraw(self, amount):
        if amount > self.__balance:
            return "Insufficient balance"
        else:
            self.__balance -= amount
            self.total_withdrawals += amount
            self.trans_history.append("Withdrawal: -" + str(amount))
            return "Withdrawal successful. New balance: " + str(self.__balance)

    def show_info(self):
        return "Acc Title: " + self.title + ", Acc No: " + str(self.accNo) + ", Balance: " + str(self.__balance)


# Inheritance
class Current(Account):
    def __init__(self, title, accNo, balance, withdrawal_limit):
        super().__init__(title, accNo, balance)
        self._withdrawal_limit = withdrawal_limit

    # Method overriding
    def show_info(self):
        base_info = Account.show_info(self)
        return "Current " + base_info + " | Limit: " + str(self._withdrawal_limit)


class Saving(Account):
    def __init__(self, title, accNo, balance, interest, minBal):
        super().__init__(title, accNo, balance)
        self._interest = interest
        self._minBal = minBal

    def get_interest_amount(self):
        return self._minBal * self._interest

    # Method overriding
    def show_info(self):
        base_info = Account.show_info(self)
        return "Saving " + base_info + " | Interest Rate: " + str(self._interest) + "%"


class Bank:
    def __init__(self):
        self.accounts = []

    def add_account(self, account):
        self.accounts.append(account)
        return "Account created successfully!"

    def get_account(self, accNo):
        for account in self.accounts:
            if account.accNo == accNo:
                return account
        return None

    def del_account(self, accNo):
        account = self.get_account(accNo)
        if account:
            balance = account.show_bal()
            if balance == 0:
                self.accounts.remove(account)
                return "Account " + str(accNo) + " deleted successfully."
            else:
                account.withdraw(balance)
                self.accounts.remove(account)
                return "Remaining balance of " + str(balance) + " withdrawn. Account " + str(accNo) + " deleted successfully."
        return "Account " + str(accNo) + " not found."


if __name__ == "__main__":
    my_bank = Bank()

    while True:
        print("\nBank Management System")
        print("=====================================")
        print("1 - Open an Account")
        print("2 - Close an Account")
        print("3 - Withdraw an Amount")
        print("4 - Deposit an Amount")
        print("5 - Show List of Accounts")
        print("6 - Transaction history of an account")
        print("7 - Total Withdrawal of an account")
        print("8 - Total Deposit amount of an account")
        print("9 - Exit")

        choice = input("\nEnter your choice (1-9): ")

        if choice == '1':
            title = input("Enter account title: ")
            accNo = input("Enter account number: ")
            balance = float(input("Enter initial balance: "))
            accType = input("Enter account type (Current/Saving): ")

            if accType.lower() == 'current':
                limit = float(input("Enter daily withdrawal limit: "))
                new_acc = Current(title, accNo, balance, limit)
                print(my_bank.add_account(new_acc))

            elif accType.lower() == 'saving':
                interest = float(input("Enter interest rate: "))
                minBal = float(input("Enter minimum balance to maintain: "))
                new_acc = Saving(title, accNo, balance, interest, minBal)
                print(my_bank.add_account(new_acc))
            else:
                print("Invalid account type.")

        elif choice == '2':
            accNo = input("Enter account number to close: ")
            print(my_bank.del_account(accNo))

        elif choice == '3':
            accNo = input("Enter account number: ")
            acc = my_bank.get_account(accNo)
            if acc:
                amount = float(input("Enter amount to withdraw: "))

                if(isinstance(acc, Current) and amount > acc._withdrawal_limit):
                    print("Withdrawal amount exceeds the daily limit of " + str(acc._withdrawal_limit))
                else:
                    print(acc.withdraw(amount))
            else:
                print("Account not found.")

        elif choice == '4':
            accNo = input("Enter account number: ")
            acc = my_bank.get_account(accNo)
            if acc:
                amount = float(input("Enter amount to deposit: "))
                print(acc.deposit(amount))
            else:
                print("Account not found.")

        elif choice == '5':
            if len(my_bank.accounts) == 0:
                print("No accounts exist currently.")
            else:
                print("\n--- List of Accounts ---")
                for acc in my_bank.accounts:
                    print(acc.show_info())

        elif choice == '6':
            accNo = input("Enter account number: ")
            acc = my_bank.get_account(accNo)
            if acc:
                print("\n Transaction History for " + str(accNo) + " ---")
                if len(acc.trans_history) == 0:
                    print("No transactions yet.")
                else:
                    for trans in acc.trans_history:
                        print(trans)
            else:
                print("Account not found.")

        elif choice == '7':
            accNo = input("Enter account number: ")
            acc = my_bank.get_account(accNo)
            if acc:
                print("Total Amount Withdrawn from " + str(accNo) + ": " + str(acc.total_withdrawals))
            else:
                print("Account not found.")

        elif choice == '8':
            accNo = input("Enter account number: ")
            acc = my_bank.get_account(accNo)
            if acc:
                print("Total Amount Deposited to " + str(accNo) + ": " + str(acc.total_deposits))
            else:
                print("Account not found.")

        elif choice == '9':
            print("Exiting Bank Management System. Goodbye!")
            break

        else:
            print("Invalid choice. Please select from 1 to 9.")
