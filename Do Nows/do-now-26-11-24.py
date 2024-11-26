# De-bug the following program
# there are five errors
# syntax or logic errors
# Challenge - develop the program
# so that it continues to play until you enter 'end'
import random

while True:
    coin = random.choice(["h", "t"])
    guess = input("Enter (h)eads or (t)ails: ")
    if guess == coin:
        print("You win")
    else:
        print("Bad luck")
    if coin == "h":
        print("It was heads")
    else:
        print("It was tails")
    
    again = input("Do you want to play again? (y/n) ").lower()
    if again == "y":
        continue
    elif again == "n":
        break

