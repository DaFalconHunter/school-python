import random
compchoice = random.choice(["R","P","S"])
print("Pick one of the following")
print()
print("(R or r) Rock")
print("(P or p) Paper")
print("(S or s) Scissors")
userchoice = input("Enter R, P or S or r, p, s alternatively: ")

play = True

if compchoice == "R":
    print("I selected...Rock")
elif compchoice == "P":
    print("I selected...Paper")
else:
    print("I selected...Scissors")
if userchoice == "R" or userchoice == "r":
    print("You selected...Rock")
elif userchoice == "P" or userchoice == "p":
    print("You selected...Paper")
elif userchoice == "S" or userchoice == "s":
    print("You selected...Scissors")
else:
    print("Incorrect selection")
    print("Try again next time when you know how to read.")
    play = False

if play == True:
    if compchoice == "R":
        if userchoice == "R" or userchoice == "r":
            print("It is a draw")
        elif userchoice == "P" or userchoice == "p":
            print("Paper wraps rock, you win")
        else:
            print("Rock blunts scissors, I win")
    if compchoice == "P":
        if userchoice == "R" or userchoice == "r":
            print("Paper wraps rock, I win")
        elif userchoice == "P" or userchoice == "p":
            print("It is a draw")
        else:
            print("Scissors cuts paper, you win")
    if compchoice == "S":
        if userchoice == "R" or userchoice == "r":
            print("Rock blunts scissors, you win")
        elif userchoice == "P"  or userchoice == "p":
            print("Scissors cuts paper, I win")
        else:
            print("It is a draw")
