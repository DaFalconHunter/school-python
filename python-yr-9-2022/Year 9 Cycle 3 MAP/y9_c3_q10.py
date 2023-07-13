# Year 9 Cycle 3 - Question 10
# Task 1 - Run the program and debug - syntax and logic errors 👍
# Task 2 - Make corrections on your assessment paper in green pen 👍
# Task 3 - Add to the program to work out the area of a rectangle, circle or other shape 👍

print("1) Square")
print("2) Triangle")
print()
menuselection = int(input("Enter a number: "))
if menuselection == 1:
    side = int(input("Enter the length of one side:"))
    area = side * side
    print("The areas of your chosen shape is ", area)
elif menuselection == 2:
    base = int(input("Enter the length of the base: "))
    height = int(input("Enter the length of the height: "))
    area = (base * height) / 2
    print("The areas of your chosen shape is ", area)
else:
    print("Incorrect option selected")
