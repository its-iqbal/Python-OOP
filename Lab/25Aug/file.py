class Shape:
    def __init__(self, color, isfilled=False):
        self.color = color
        self.isfilled = isfilled

    def fill_color(self):
        if self.isfilled == False:
            self.isfilled = True

    def show_info(self):
        print(f"Color: {self.color}, Filled: {self.isfilled}")

class Circle(Shape):
    def __init__(self, r, c, isfilled=False):
        super().__init__(c, isfilled)
        self.r = r

    def calculate_area(self):
        return 3.14 * self.r ** 2

    def show_info(self):
        super().show_info()
        print(f"Radius: {self.r}, Area: {self.calculate_area()}")

class Square(Shape):
    def __init__(self, s,c, isfilled=False):
        super().__init__(c, isfilled)
        self.side = s

    def calculate_area(self):
        return self.side ** 2

    def show_info(self):
        super().show_info()
        print(f"Side: {self.side}, Area: {self.calculate_area()}")

class Rectangle(Shape):
    def __init__(self, w, h, c, isfilled=False):
        super().__init__(c, isfilled)
        self.width = w
        self.height = h

    def calculate_area(self):
        return self.width * self.height

    def show_info(self):
        super().show_info()
        print(f"Width: {self.width}, Height: {self.height}, Area: {self.calculate_area()}")

class Triangle(Shape):
    def __init__(self, b, h, c, isfilled=False):
        super().__init__(c, isfilled)
        self.base = b
        self.height = h

    def calculate_area(self):
        return 0.5 * self.base * self.height

    def show_info(self):
        super().show_info()
        print(f"Base: {self.base}, Height: {self.height}, Area: {self.calculate_area()}")
        