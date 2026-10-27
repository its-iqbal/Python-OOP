class A:
    def __init__(self):
        self.name = "Class A"

    def show(self):
        print("This is from A")

class B(A):
    def __init__(self):
        super().__init__()
        self.name = "Class B"

    def show(self):
        print("This is from B")
        super().show()

class C(A):
    def __init__(self):
        super().__init__()
        self.name = "Class C"

    def show(self):
        print("This is from C")
        super().show()

class D(B, C):
    def __init__(self):
        super().__init__()
        self.name = "Class D"

    def show(self):
        print("This is from D")
        super().show()

class E(C):
    def __init__(self):
        super().__init__()
        self.name = "Class E"

    def show(self):
        print("This is from E")
        super().show()

class F(D, E):
    def __init__(self):
        super().__init__()
        self.name = "Class F"

    def show(self):
        print("This is from F")
        super().show()

class G(E):
    def __init__(self):
        super().__init__()
        self.name = "Class G"

    def show(self):
        print("This is from G")
        super().show()

class X(F, G):
    def __init__(self):
        super().__init__()
        self.name = "Class X"

    def show(self):
        print("This is from X")
        super().show()

obj = X()
obj.show()