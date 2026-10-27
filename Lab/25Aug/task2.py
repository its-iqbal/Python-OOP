from file import Circle, Triangle, Square, Rectangle

sum = 0
choice = True
while choice == True:
    list = []

    num = int(input("Write (1-4) number for shapes: "))

    if num == 1:
        r = float(input("Enter radius of circle: "))
        c = input("Enter color of circle: ")
        f = input("Do you want to fill the circle? (y/n): ")
        if f == "y":
            obj = Circle(r, c, isfilled=True)
            list.append(obj)
        else:
            obj = Circle(r, c)
            list.append(obj)
    elif num == 2:
        s = float(input("Enter side of square: "))
        c = input("Enter color of square: ")
        f = input("Do you want to fill the square? (y/n): ")
        if f == "y":
            obj = Square(s, c, isfilled=True)
            list.append(obj)
        else:
            obj = Square(s, c)
            list.append(obj)
    elif num == 3:
        w = float(input("Enter width of rectangle: "))
        h = float(input("Enter height of rectangle: "))
        c = input("Enter color of rectangle: ")
        f = input("Do you want to fill the rectangle? (y/n): ")
        if f == "y":
            obj = Rectangle(w, h, c, isfilled=True)
            list.append(obj)
        else:
            obj = Rectangle(w, h, c)
            list.append(obj)
    elif num == 4:
        b = float(input("Enter base of triangle: "))
        h = float(input("Enter height of triangle: "))
        c = input("Enter color of triangle: ")
        f = input("Do you want to fill the triangle? (y/n): ")
        if f == "y":
            obj = Triangle(b, h, c, isfilled=True)
            list.append(obj)
        else:
            obj = Triangle(b, h, c)
            list.append(obj)
    elif num >= 5:
        print("Number of shapes exceed")

    obj.show_info()

    for shape in list:
        if shape.isfilled == True:
            sum += shape.calculate_area()

    choice = input("Do you want to continue? (y/n): ")
    if choice == "n":
        choice = False
        print(f"Total area: {sum}")
    else:
        choice = True
        
