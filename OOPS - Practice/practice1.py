# class Book:
#     def __init__(self, title, author, pages):
#         self.title = title
#         self.author = author
#         self.pages = pages
#         self.current_page = 0

#     def read(self, pages_read):
#         self.current_page += pages_read

#         if self.current_page > self.pages:
#             self.current_page = self.pages
#             print("Page Limit exceed and set to max")

#     def show(self):
#         print(f"Iqbal is {(self.current_page/self.pages)*100:.1f}% through {self.title}")

# reader = Book("Dune", "JK Rowling", 300)
# reader.read(200)
# reader.read(50)
# reader.read(100)

# reader.show()

#--------------------------------------------------------

# class Thermometer:
#     def __init__(self, celsius):
#         self.celsius = celsius        # goes through the setter

#     @property
#     def celsius(self):
#         return self._celsius

#     @celsius.setter
#     def celsius(self, val):
#         if val < -273.15:
#             raise ValueError("Temperature cannot be below absolute zero")
#         else:
#             self._celsius = val

#     @property
#     def fahrenheit(self):
#         return self.celsius * 9/5 + 32

# temp = Thermometer(-500)
# # res = temp.celsius = 100
# # print(res)
# fah = temp.fahrenheit
# print(fah)

#----------------------------------------------------

class Employee:
    def __init__(self, name, base_sal):
        self.name = name
        self.__base_sal = base_sal

    @property
    def base_sal(self):
        return self.__base_sal

class Manager(Employee):
    def __init__(self, name, base_sal, bonus):
        super().__init__(name, base_sal)
        self.bonus = bonus

    def base_sal(self):
        return super().base_sal + self.bonus

class Intern(Employee):
    def __init__(self, name, base_sal):
        super().__init__(name, base_sal)

    def base_sal(self):
        return super().base_sal * 0.5

mang = Manager("Ali", 50000, 5000)
print(mang.base_sal())

inte = Intern("Iqbal", 30000)
print(inte.base_sal())