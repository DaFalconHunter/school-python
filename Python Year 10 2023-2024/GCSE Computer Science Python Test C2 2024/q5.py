#Question 5
#Write a program that generates two random numbers.
#The user then inputs which arithmetic operator they want
#to use to perform a calculation between the two numbers, +  -  /  *.
#The calculation is then performed and the output printed.

import random

num1 = random.randint(1, 100)
num2 = random.randint(1, 100)
print(f"Your numbers: no.1 = {num1}; no.2 = {num2}")
operator = input("Enter the operation I will conduct (+, -, *, /): ")
while True:
    match operator:
        case "+":
            calc = num1 + num2
            break
        case "-":
            calc = num1 - num2
            break
        case "*":
            calc = num1 * num2
            break
        case "/":
            calc = num1 / num2
            break
        case _:
            operator = input("Please enter your desired operator: ")

print(calc)