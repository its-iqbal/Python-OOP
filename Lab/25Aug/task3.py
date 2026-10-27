from file import Circle, Triangle, Square, Rectangle

sum = 0
total_shapes = 0
total_circles = 0
total_squares = 0
total_rectangles = 0
total_triangles = 0
total_filled_shapes = 0
total_unfilled_shapes = 0
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
    else:
        print("Number of shapes exceed")
        continue

    obj.show_info()

    total_shapes += 1
    if isinstance(obj, Circle):
        total_circles += 1
    elif isinstance(obj, Square):
        total_squares += 1
    elif isinstance(obj, Rectangle):
        total_rectangles += 1
    elif isinstance(obj, Triangle):
        total_triangles += 1

    if obj.isfilled:
        total_filled_shapes += 1
    else:
        total_unfilled_shapes += 1

    for shape in list:
        if shape.isfilled:
            sum += shape.calculate_area()

    choice = input("Do you want to continue? (y/n): ")
    if choice == "n":
        choice = False
        print(f"Total area: {sum}")
        print(f"Total Shapes: {total_shapes}")
        print(f"Total Circles: {total_circles}")
        print(f"Total Squares: {total_squares}")
        print(f"Total Rectangles: {total_rectangles}")
        print(f"Total Triangles: {total_triangles}")
        print(f"Total Filled Shapes: {total_filled_shapes}")
        print(f"Total Unfilled Shapes: {total_unfilled_shapes}")
    else:
        choice = True
        
