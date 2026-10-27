class Faculty:
    def __init__(self):
        self.salary = 0
        
    def calculate_salary(self):
        pass

class FullTimeFaculty(Faculty):

    def __init__(self, designation):
        super().__init__()
        self.base_salary = 75000
        self.designation = designation

    def calculate_salary(self):
        if self.designation == "Lecturer":
            allowance = 50000
        elif self.designation == "Assistant Professor":
            allowance = 75000
        elif self.designation == "Associate Professor":
            allowance = 150000
        elif self.designation == "Professor":
            allowance = 225000
        else:
            print(f"Invalid designation")
            allowance = 0

        self.salary = self.base_salary + allowance
        return self.salary

class VisitingFaculty(Faculty):

    def __init__(self, hours, fac_type):
        super().__init__()
        self.hours = hours
        self.fac_type = fac_type

    def calculate_salary(self):
        if self.fac_type == "Industry Professionals":
            rate = 2000
        elif self.fac_type == "Interdepartmental Teachers":
            rate = 1000
        else:
            print(f"Invalid faculty type")
            rate = 0

        self.salary = self.hours * rate
        return self.salary
    
class HEI:
    def __init__(self):
        self.faculty_members = []
        self.budget = 10000000
        self.total_visiting_remuneration = 0

    def add_faculty(self, faculty):
        salary = faculty.calculate_salary()
        if self.budget >= salary:
            self.faculty_members.append(faculty)
            self.budget -= salary
            print(f"Faculty added. Remuneration: Rs. {salary}")
            print(f"Remaining Budget: Rs. {self.budget}")
            
            if isinstance(faculty, VisitingFaculty):
                self.total_visiting_remuneration += salary
        else:
            print("Remaining budget is not enough to hire this faculty member.")
            return False
        return True

    def show_all_remunerations(self):
        print("All Faculty Remunerations")
        for fac in self.faculty_members:
            print(f"Salary: Rs. {fac.calculate_salary()}")

    def show_visiting_total(self):
        print(f"Total Remuneration paid to Visiting Faculty: Rs. {self.total_visiting_remuneration}")
        

def main():
    hei = HEI()
    
    while hei.budget > 0:
        print("Higher Education Institute Faculty Remuneration System")
        print("1. Full-time Faculty")
        print("2. Visiting Faculty")
        print("3. Exit and Show Reports")
        
        choice = input("Enter choice (1/2/3): ")
        
        if choice == '1':
            print("Designations: Lecturer, Assistant Professor, Associate Professor, Professor")
            designation = input("Enter designation: ")
            faculty = FullTimeFaculty(designation)
            hei.add_faculty(faculty)
            
        elif choice == '2':
            print("Types: Industry Professionals, Interdepartmental Teachers")
            fac_type = input("Enter type: ")
            hours = int(input("Enter teaching hours: "))
            faculty = VisitingFaculty(hours, fac_type)
            hei.add_faculty(faculty)
            
        elif choice == '3':
            break
        else:
            print("Invalid choice.")
            
    hei.show_all_remunerations()
    hei.show_visiting_total()

if __name__ == "__main__":
    main()