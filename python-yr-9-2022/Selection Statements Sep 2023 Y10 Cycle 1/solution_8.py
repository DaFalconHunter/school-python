num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))

if num1 % 2 != 0 and num2 % 2 != 0:
    print("Both of these numbers are odd")
elif num1 % 2 != 0 or num2 % 2 != 0:
    print("At least one of these numbers is odd")
elif num1 % 2 == 0 and num2 % 2 == 0:
    print("Both of these numbers are even")