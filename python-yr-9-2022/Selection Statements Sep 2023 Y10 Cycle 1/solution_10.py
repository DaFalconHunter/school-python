num1 = int(input("Enter the 1st number: "))
num2 = int(input("Enter the 2nd number: "))
num3 = int(input("Enter the 3rd number: "))

user_input = [num1, num2, num3]
ascending = sorted(user_input)

if user_input == ascending:
    print("This list is in ascending order")
else:
    print("This list is not in ascending order")
