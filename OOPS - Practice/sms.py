class Person:
    def __init__(self, name, id_number):
        self.name = name
        self.__id_no = id_number

    def get_details(self):
        return f"Name: {self.name}, Id: {self.__id_no}"

per1 = Person("Iqbal", 1480688)
# print(per1.get_details())

class Student(Person):
    def __init__(self, name, id_number, grade):
        super().__init__(name, id_number)
        self.grade = grade

    def get_details(self):
        return f"{super().get_details()} | Grade: {self.grade}"

std1 = Student("Iqbal", 1480688, 10)
# print(std1.get_details())

class Teacher(Person):
    def __init__(self, name, id_number, subject):
        super().__init__(name, id_number)
        self.subject = subject

    def get_details(self):
        return f"{super().get_details()} | Subject: {self.subject}"

teh1 = Teacher("Iqbal", 6, "English")
# print(teh1.get_details())

class School:
    def __init__(self):
        self.members = []

    def add_member(self, person):
        self.members.append(person)

    def roll_call(self):
        for mem in self.members:
            if isinstance(mem, Student):
                print(f"{mem.get_details()} | Details - ENROLLED")
            elif isinstance(mem, Teacher):
                print(f"{mem.get_details()} | Details - STAFF")
            elif isinstance(mem, Person):
                print(f"{mem.get_details()} | Details - PERSON")
            else:
                print("Invalid")

Sch = School()

Sch.add_member(teh1)
Sch.add_member(std1)
Sch.add_member(per1)

Sch.roll_call()
