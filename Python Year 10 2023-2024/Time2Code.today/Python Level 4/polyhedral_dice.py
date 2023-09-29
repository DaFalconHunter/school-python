# Polyhedral dice program

# -------------------------
# Import libraries
# -------------------------
import random


# -------------------------
# Subprograms
# -------------------------
def roll_dice(input_sides):
    return random.randint(1, input_sides)


# -------------------------
# Main program
# -------------------------
random.seed()
num_sides = int(input("Enter the number of sides on the dice you want to roll: "))
number = roll_dice(num_sides)
print("You rolled a", number)
