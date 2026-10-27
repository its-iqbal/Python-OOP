class A:
    def __init__(self):
        self.name = "Class A"

    @classmethod
    def show(cls):
        print("This is from A")

class B(A):
    def __init__(self):
        super().__init__()
        self.name = "Class B"

    @classmethod
    def show(cls):
        print("This is from B")
        super().show()

obj = B()
obj.show()