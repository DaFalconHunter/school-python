# Title - Average of scores input by the user Version 1.
# Do Now - run the program a couple of times to check how it works.
# At the beginning of each of the 5 sections there is a #.
# Use this to explain what that section of code is doing.

# 1.
totalScore = 0
numScore = 0
moreScores = True

# 2.
while moreScores:
    score = int(input("Enter the next score, -1 to end: "))

    # 3.
    if score != -1:
        numScore = numScore + 1
        totalScore = totalScore + score
    else:
        moreScores = False
# 4.
if numScore == 0:
    print("\nNo scores entered - program ended")
else:
    averageScore = totalScore / numScore
    print("\nAverage score: ", averageScore)

# 5.
input("\nPress ENTER to exit program ")
