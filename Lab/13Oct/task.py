class Employee:
    def __init__(self, name, position, acc_no):
        self.name = name
        self.position = position
        self.acc_no = acc_no


class Bank:
    def __init__(self):
        self.position = ["Manager", "Accountant", "Cashier", "Guard"]
        self.employees = []

    def add_employee(self, name, position, acc_no):
        employee = Employee(name, position, acc_no)
        self.employees.append(employee)
        return employee

    def find_employee(self, name, acc_no):
        for employee in self.employees:
            if employee.name == name and employee.acc_no == acc_no:
                return employee
        return None

    def transfer_salary(self, name, acc_no):
        employee = self.find_employee(name, acc_no)
        if employee is not None:
            print(f"Salary transferred to {employee.name} with account number {employee.acc_no}.")
        else:
            print(f"No employee found with name {name} and account number {acc_no}.")


class HEI:
    def __init__(self, name, location, bank):
        self.name = name
        self.location = location
        self.bank = bank

    def pay_sal(self, name, acc_no):
        employee = self.bank.find_employee(name, acc_no)
        if employee is not None:
            print(f"Salary paid to {employee.name} from {self.name} to account number {employee.acc_no}.")
        else:
            print(f"No employee found with name {name} and account number {acc_no}.")


if __name__ == "__main__":
    bank = Bank()
    bank.add_employee("Ali", "Manager", "1001")
    bank.add_employee("Sara", "Accountant", "1002")

    ubit = HEI("University of Business and Information Technology", "City Center", bank)

    bank.transfer_salary("Ali", "1001")
    ubit.pay_sal("Sara", "1002")

