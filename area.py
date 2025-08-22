print("menu:")
print("1.find area of circle:")
print("2.find area of triangle:")
print("3.find area of square:")
print("4.find area pf rectangle:")
print("5.exist")

while True:
    choice = int(input("Enter your choice: (1-6);"))

    if choice == 1:
        radius = float(input("Enter the radius of the circle: "))
        area = 3.14 * radius * radius
        print(f"The area of the circle is: {area}")

    elif choice == 2:   
        base = float(input("Enter the base of the triangle: "))
        height = float(input("Enter the height of the triangle: "))
        area = 0.5 * base * height
        print(f"The area of the triangle is: {area}")  

    elif choice == 3:
        side = float(input("Enter the side length of the square: "))    
        area = side * side
        print(f"The area of the square is: {area}")

    elif choice == 4:
        length = float(input("Enter the length of the rectangle: "))
        width = float(input("Enter the width of the rectangle: "))
        area = length * width   
        print(f"The area of the rectangle is: {area}")
        
    elif choice == 5:
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
