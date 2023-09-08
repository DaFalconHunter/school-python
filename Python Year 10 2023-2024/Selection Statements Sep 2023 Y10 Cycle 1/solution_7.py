num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))

if num1 % 2 != 0 or num2 % 2 != 0:
    print("At least one of these numbers is odd")
else:
    print("Not one of these numbers is odd")