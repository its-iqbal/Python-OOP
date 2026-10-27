class A:
    inst = None

    def __new__(cls, a, b):
        if A.inst is None:
            A.inst = super().__new__(cls)

        else:
            print("Instance already exists. Returning the existing instance.")
        return A.inst

    def __init__(self, a, b):
        self.a = a
        self.b = b

obj1 = A(5, 6)
obj2 = A(7, 8)

print(obj1.a, obj1.b)  # Output: 5 6
print(obj2.a, obj2.b)  # Output: 5 6
