#While loop challenge 3

#Rearrange the four lines of code below.
#to get the while loop to work.
#It should keep asking "Press 1 for choice or 2 to exit".
#until "2" is entered.
#You might need to indent some lines.

StayInLoop = 1
while StayInLoop != 2:
    print("Press 1 for  choice or 2 to exit")
    StayInLoop = int(input("Please respond, 1 or 2: "))
print("Exited")
