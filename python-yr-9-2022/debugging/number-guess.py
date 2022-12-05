import random
compnum = random.randint(1,100)
playagain = True
guesses = 0
while playagain == True:
    usernum = int(input("Guess a number:" ))
    if usernum == compnum:
        print("Correct")
        playagain = False
        guesses += 1
    elif usernum > compnum:
        print("Too high")
        guesses += 1
    else:
        print("Too low")
        guesses += 1
print("You took", guesses, "turns to get it right")
