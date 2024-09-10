# Multiplication tables test (while loop and elif)
# There are 5 errors, debug the program and test until fully working.

import random

print("Multiplication tables test")
print("**********************\n")
print("What table would you like to be tested on?")
timestable = int(input(""))
print("You will be given 5 questions")

score = 0
loopcounter = 1
while loopcounter <= 5:
    number = random.randint(3, 12)
    print(timestable, "X", number, "?")
    useranswer = int(input())
    correctanswer = number * timestable
    loopcounter += 1
    if useranswer == correctanswer:
        score += 1
        print("Correct")
    else:
        print("Wrong! The correct answer is", correctanswer)

if score == 5:
    print("Congratulatios! You scored", score, "out of 5")
elif score == 4:
    print("Pretty good... you scored", score, "out of 5")
elif score == 3:
    print("Could do better... you scored", score, "out of 5")
else:
    print("Oh dear! Back to the drawing board... you scored", score, "out of 5")

input("\n\nPress ENTER to exit")