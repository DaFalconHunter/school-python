#  Question 1:
answer = input("Q1) What is the capital of France? ").title()
counter = 1

while answer != "Paris":
    answer = input("Incorrect, try again: ").title()
    counter += 1

print("Correct! Well done.")
print("It took you " + str(counter) + " attempts to get the answer right")

#  Question 2:
answer = input("\nQ2) What is the name of the current Prime Minister? ").title()
counter = 1

while answer != "Boris Johnson":
    answer = input("Incorrect, try again: ").title()
    counter += 1

print("Correct! Well done.")
print("It took you " + str(counter) + " attempts to get the answer right")

#  Question 3:
answer = input("\nQ3) What year was the Paris Climate Agreement held? ").title()
counter = 1

while answer != "2015":
    answer = input("Incorrect, try again: ").title()
    counter += 1

print("Correct! Well done.")
print("It took you " + str(counter) + " attempts to get the answer right")

#  Question 4:
answer = input("\nQ4) Where is the Last Untouched Wilderness? ").title()
counter = 1

while answer != "Antarctica":
    answer = input("Incorrect, try again: ").title()
    counter += 1

print("Correct! Well done.")
print("It took you " + str(counter) + " attempts to get the answer right")
