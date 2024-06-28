#While loop challenge 8

# Part of this code is missing.
# It should ask the user to guess a number over and over again, but..
# only give them 5 attempts.
# If they guess correct, it displays 'Yay! Correct guess'
# otherwise it prints ''
# HINT: Use an "and" operator.


import random
number = random.randint(1,10)
attempts = 0

#add a While loop here
while attempts < 6:
    guess = int(input("Make a guess from 1-10: "))
    attempts += 1
    if guess == number:
        print("Yay! Correct guess")
        break
    elif attempts == 5:
        print("You are out of attempts")
        break
    else:
        continue
