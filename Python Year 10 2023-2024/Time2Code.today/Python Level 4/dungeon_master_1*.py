# Dungeon master program

# -------------------------
# Import libraries
# -------------------------
import random

# -------------------------
# Subprograms
# -------------------------
# Function to return if a skill check is passed in DnD5e
def check_skill(skill, modifier, dm_value):
    roll = random.randint(1, 20)
    if (skill + modifier) >= (dm_value + 5):
        return "Automatic pass"   
    print(f"You rolled a {roll}")
    if roll == 1:
        return "Critical fail"
    elif roll == 20:
        return "Critical success"
    elif (skill + roll + modifier) >= dm_value:
        return "Check passed"
    elif (skill + roll + modifier) < dm_value:
        return "Check failed"

# -------------------------
# Main program
# -------------------------

skill = int(input("Enter the skill value: "))
modifier = int(input("Enter any modifiers: "))
dm_value = int(input("Enter the Dungeon Master's pass number: "))

result = check_skill(skill, modifier, dm_value)
print(result)
