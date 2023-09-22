# Display the following message:
# 1) Square
# 2) Triangle
# Enter a number:
# If the user enters 1, then it should ask them for the length of
# one of its sides and display the area.
# If they select 2, it should ask for the base and the height of
# a triangle and display the area.
# If they type in anything else, it should give them a suitable error message.

def square(side):
    return side**2

def triangle(base, height):
    return (base * height) / 2

def calc():
    print("(1) Square\n(2) Triangle")
    selection = int(input("Enter a number: "))
    if selection == 1:
        side_input = float(input("Enter the length of a side: "))
        print(f"The area of a square with side length \n{side_input} is {square(side_input)} square units")
        return True
    elif selection == 2:
        base_input = float(input("Enter the base length: "))
        height_input = float(input("Enter the height: "))
        print(
            f"The area of a triangle with base length {base_input} and height {height_input} is {triangle(base_input, height_input)} square units"
        )
        return True
    else:
        print("Please enter either 1 or 2")
        return False

def run_again():
    calc_again = input("Would you like to make another calculation? (y/n): ").lower()
    if calc_again == "y":
        return True
    elif calc_again == "n":
        return False
    else:
        print("Please enter either (y)es or (n)o")

while True:
    while calc() != True:
        calc()
    if run_again() == False:
        break
    else:
        run_again()
