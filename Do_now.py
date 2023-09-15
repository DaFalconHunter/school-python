#DO NOW
#Add the following lines of code.
#1. Ask a user to input their name and assign to the variable name
#2. Ask a user to enter a number and assign to the variable num1
#3. Ask a user to enter a number and assign to the variable num2
#4. Print the following calculations:
#Two numbers added together.
#Two number multiplied.
#Num1 divded by num2.
#Num1 subtracted from num2.
#The remainder of one number divided by the other.
#The whole number of one number divided by the other.

name = input("Enter your name: ")
num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))

print(f"{num1} + {num2} = " + str(num1 + num2))
print(f"{num1} * {num2} = " + str(num1 * num2))
print(f"{num1} / {num2} = " + str(num1 / num2))
print(f"{num1} - {num2} = " + str(num1 - num2))
print(f"{num1} % {num2} = " + str(num1 % num2))
print(f"{num1} // {num2} = " + str(num1 // num2))