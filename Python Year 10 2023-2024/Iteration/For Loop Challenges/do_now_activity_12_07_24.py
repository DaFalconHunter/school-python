# Title - Average of scores input by the user Version 1.
# Do Now - run the program a couple of times to check how it works.
# At the beginning of each of the 5 sections there is a #.
# Use this to explain what that section of code is doing.

# 1. Initialise variables: sum of scores (totalScore), no. of inputted scores (numScore), and condition if more scores are to be inputted (moreScores).
totalScore = 0
numScore = 0
moreScores = True

# 2. Loop while program needs more scores
while moreScores:
    score = int(input("Enter the next score, -1 to end: "))

    # 3. Increment no. of inputted scores by 1, and add the inputted score to the totalScore variable
    if score != -1:
        numScore = numScore + 1
        totalScore = totalScore + score
    else:
        moreScores = False
# 4. If no scores are entered, end the program, otherwise calculate an average. 
if numScore == 0:
    print("\nNo scores entered - program ended")
else:
    averageScore = totalScore / numScore
    print("\nAverage score: ", averageScore)

# 5. Code to cease the program.
input("\nPress ENTER to exit program ")
