# While loop challenge 6

# There is a line of code missing below.
# The point of al the code is to generate a random number, then
# asks the user to try and guess it
# Can you fix it?
# Look through the code then enter a fix below.


import random

number = random.randint(1, 10)
userGuess = int(input("Guess the number between 1-10: "))

# Add one line of code here to allow the user to
# Hint: You might need to indent some code

if number < userGuess:
    guess = int(input("Guess too High, try again: "))
else:
    guess = int(input("Guess too Low, try again: "))

print("Yay! You got it correct!!!")
