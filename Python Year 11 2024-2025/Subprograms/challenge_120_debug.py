#Challenge 120
#Run the code and debug - 2 syntax errors and 2 logic errors
#Comment on the code to show what each section is doing

import random

# Addition function that generates two random numbers between 5 and 20, asks the user for their answer, and returns
# both the user's answer and the actual answer
def addition():
    num1 = random.randint(5,20)
    num2 = random.randint(5,20)
    print(num1, "+", num2, "= ")
    user_answer = int(input("your answer: "))
    actual_answer = num1 + num2
    answers = (user_answer, actual_answer)
    return answers

# Subtraction function that generates two random numbers, the first between 25 and 50 and the second between 1 and 25,
# asks the user for their answer, and returns both the user's answer and the actual answer
def subtraction():
    num3 = random.randint(25,50)
    num4 = random.randint(1,25)
    print(num3, "-", num4, "= ")
    user_answer = int(input("your answer: "))
    actual_answer = num3 - num4
    answers = (user_answer, actual_answer)
    return answers

# Check the user's answer against the actual answer and print whether it is correct or incorrect
def check_answer(user_answer, actual_answer):
    if user_answer == actual_answer:
        print("Correct")
    else:
        print("Incorrect, the answer is", actual_answer)

# Main function that presents the user with a choice of addition or subtraction, calls the appropriate function,
# and checks the user's answer.
def main():
    print("1) Addition")
    print("2) Subtraction")
    selection = int(input("Enter 1 or 2: "))
    if selection == 1:
        user_answer, actual_answer = addition()
        check_answer(user_answer, actual_answer)
    elif selection ==2:
        user_answer, actual_answer = subtraction()
        check_answer(user_answer, actual_answer)
    else:
        print("Incorrect section")
main()
