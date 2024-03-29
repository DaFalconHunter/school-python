# Guess the number program

# -------------------------
# Import libraries
# -------------------------
import random

# -------------------------
# Subprograms
# -------------------------
def play_guess_the_number(minimum, maximum):
    random_num = random.randint(minimum, maximum)
    guess = int(input("Guess the number between 1 & 100: "))
    num_guesses = 1
    while guess != random_num:        
        if random_num >= guess:
            print("Your guess was too low")
            num_guesses += 1
            guess = int(input("Guess the number between 1 & 100: "))
        elif random_num <= guess:
            print("Your guess was too high")
            num_guesses += 1
            guess = int(input("Guess the number between 1 & 100: "))
        elif random_num == guess:
            break
    if random_num == guess:
        print(f"It took you {num_guesses} guesses.")
        print("You guessed correctly!")

# -------------------------
# Main program
# -------------------------
play_guess_the_number(1, 100)
