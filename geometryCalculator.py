shape = input("Choose a shape!(rectangle, triangle, circle) ")

if shape.lower() == "rectangle":
    base = input("What is the base of the rectangle? ")
    height = input("What is the height of the rectangle? ")
    area = int(base) * int(height)
    print(f"The area of your rectangle is {area} units.")
elif shape.lower() == "triangle":
    base = input("What is the base of the triangle? ")
    height = input("What is the height of the triangle? ")
    area = int(base) * int(height)
    print(f"The area of your triangle is {area/2} units.")
elif shape.lower() == "circle":
    radius = input("What is the radius of the circle? ")
    area = 3.14 * int(radius) * int(radius)
    print(f"The area of your circle is about {float(area)} units.")
else:
    print("Please choose a valid shape.")
