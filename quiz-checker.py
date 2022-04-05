answer = input("What is the capital of France? ").title()
counter = 1

while answer != "Paris":
    answer = input("Incorrect, try again: ").title()
    counter += 1

print("Correct! Well done.")
print("It took you " + str(counter) + " attempts to get the answer right")