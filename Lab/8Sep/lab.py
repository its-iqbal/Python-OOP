#Multi Inheritance
class A:
    def __init__(self):
        self.name = "Class A"

    def show(self):
        print("This is from A")

class B:
    def __init__(self):
        self.name = "Class B"

    def show(self):
        print("This is from B")

class C1(A, B):
    def __init__(self):
        super().__init__(self) 
        super().__init__(self)
        self.child_att = "I am C1"

    def show(self):
        print("This is from C1")

class C2(B, A):
    def __init__(self):
        B.__init__(self)
        A.__init__(self)
        self.child_att = "I am C2"

obj1 = C1()
obj2 = C2()
obj1.show()
print("MRO of C1: ", C1.__mro__)
print("MRO of C2: ", C2.__mro__)
print("Obj1 child attribute: ", obj1.child_att)


#Counting Number of Objects by class
class Student:
    count = 0

    def __init__(self, name):
        self.name = name
        Student.count += 1

    def info(self):
        print(f"Student: {self.name}")

s1 = Student("Ali")
s2 = Student("Ahmed")
print(f"Total Objects: {Student.count}")
