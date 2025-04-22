#Challenge 119
#Run the code and debug - 2 syntax errors and 1 logic error
#Comment on each sub program to explain what their purpose is

import random

def pick_num():
    low=int(input("Enter the bottom of the range: "))
    high=int(input("Enter the top of the range: "))
    comp_num=random.randint(low,high)
    return comp_num

def first_guess()
    print("I am thinking of a number...")
    guess=int(input("What am I thinking of:  "))
    return guess

def check_answer(comp_num,guess):
    try_again = True
    while try_again == true:
        if comp_num == guess:
            print("Correct, you win.")
            try_again = False
        elif comp_num>guess:
            guess = int(input("Too low, try again: "))
        else:
            guess = int(input("Too low, try again: "))

def main():
    comp_num = pick_num()
    guess = first_guess()
    check_answer(comp_num,guess)

main()
