from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def cal_area(self):
        pass
        
class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def cal_area(self):
        return 3.14 * self.radius ** 2

class Square(Shape):

    def __init__(self, side):
        self.side = side

    def cal_area(self):
        return self.side ** 2

circle = Circle(5)
print(circle.cal_area())

square = Square(5)
print(square.cal_area())
