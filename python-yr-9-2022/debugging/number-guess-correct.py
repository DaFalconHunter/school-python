#Number guess program
#Version 2
import random
compnum=random.randint(1,100)
guesses = 0 # Added to set inital score
playagain = True # Added to allow the while loop to run
while playagain == True:
    usernum = int(input("Guess a number:" ))
    guesses = guesses + 1 # Changed to keep running score 
    if usernum == compnum:#Variable name corrected to compnum
        print("Correct")
        playagain = False
    elif usernum > compnum:# comparison symbol altered
        print("Too high")
    else:
        print("Too low")
print("You took", guesses, "turns to get it right")#comma added after guesses


    