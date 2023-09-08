num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))

if num1 > num2:
    print(f'{num2} is less than {num1}')
elif num1 == num2:
    print(f'{num1} is equal to {num2}')
else:
    print(f'{num1} is less than {num2}')