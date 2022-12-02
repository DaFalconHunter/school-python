import random
compnum=random.randint(1,100)
while playagain == True:
    usernum = int(input("Guess a number:" ))
    guesses = 1
    if usernum == comnum:
        print("Correct")
        playagain = False
    elif usernum < compnum:
        print("Too high")
    else:
        print("Too low")
print("You took", guesses "turns to get it right")
