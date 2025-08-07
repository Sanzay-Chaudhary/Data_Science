import math  # to use math.pi for circle

print("Welcome to the Area Calculator!")
print("Choose a shape:")
print("1. Square")
print("2. Rectangle")
print("3. Triangle")
print("4. Circle")

choice = input("Enter the number of your choice (1-4): ")

if choice == "1":
    side = float(input("Enter the side length of the square: "))
    area = side * side
    print("Area of the square is:", area)

elif choice == "2":
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    area = length * width
    print("Area of the rectangle is:", area)

elif choice == "3":
    base = float(input("Enter the base of the triangle: "))
    height = float(input("Enter the height of the triangle: "))
    area = 0.5 * base * height
    print("Area of the triangle is:", area)

elif choice == "4":
    radius = float(input("Enter the radius of the circle: "))
    area = math.pi * radius * radius
    print("Area of the circle is:", round(area, 2))

else:
    print("❌ Invalid choice. Please run the program again and choose from 1 to 4.")
