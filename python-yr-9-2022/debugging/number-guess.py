# Import random module:
import random
# Initialise computer's random guess
compnum = random.randint(1, 100)

# Set game run var. to True:
playagain = True

# Initialise guesses at 0:
guesses = 0

# Start game loop:
# while playagain == True: ==> Legacy code 
# ----> remove playagain var. to reduce memory footprint
while True:
    # Take user guess input:
    usernum = int(input("Guess a number: "))
    # Increment guesses:
    guesses += 1
    # Kill the loop if the user guesses correctly:
    if usernum == compnum:
        print("Correct")
        # playagain = False ==> Legacy code 
        # ----> remove playagain var. to reduce memory footprint
        break
    elif usernum > compnum: # Display comparison if incorrect:
        print("Too high")
    else:
        print("Too low")

# Game loop killed. Output no. of guesses to the user:
print("You took", guesses, "turns to get it right")
