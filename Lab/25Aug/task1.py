from file import Circle, Triangle, Square, Rectangle

sum = 0
choice = True
while choice == True:
    num = int(input("Write (1-4) number for shapes: "))

    if num == 1:
        r = float(input("Enter radius of circle: "))
        c = input("Enter color of circle: ")
        obj = Circle(r, c)
    elif num == 2:
        s = float(input("Enter side of square: "))
        c = input("Enter color of square: ")
        obj = Square(s, c)
    elif num == 3:
        w = float(input("Enter width of rectangle: "))
        h = float(input("Enter height of rectangle: "))
        c = input("Enter color of rectangle: ")
        obj = Rectangle(w, h, c)
    elif num == 4:
        b = float(input("Enter base of triangle: "))
        h = float(input("Enter height of triangle: "))
        c = input("Enter color of triangle: ")
        obj = Triangle(b, h, c)
    elif num >= 5:
        print("Number of shapes exceed")

    obj.show_info()
    sum += obj.calculate_area()

    choice = input("Do you want to continue? (y/n): ")
    if choice == "n":
        choice = False
        print(f"Total area: {sum}")
    else:
        choice = True
        
