# Question 6b
# Complete line C to generate a 4 digit number between 1000 and 9999
# Line 6 has two syntax errors, correct the code.
# Use .upper to make the program robust.
# Upload your completed solution to Teams.

import random
a = input("Enter first letter of first name") 
b = input("Enter first letter of second name") 
c = random.randint(1, 1000)
again = "Y"
while again == "Y":
    pilotCode = a + b + str(c)
    print(pilotCode)
    again = input("Do you want to generate another code? ")
print("Goodbye")
