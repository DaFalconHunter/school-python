studentnames = ["Rob", "Anna", "Huw", "Emma", "Patrice", "Iqbal"]

num_present = 0
num_absent = 0

for name in studentnames:
    print(f"Name: {name}")
    present_or_absent = input(f"Is {name} present or absent? (p/a): ").lower()
    
    if present_or_absent == "p":
        num_present += 1
    elif present_or_absent == "a":
        num_absent += 1
    else:
        print("Invalid input. Please enter 'p' or 'a'.")

print(f"There are {num_present} students present and {num_absent} students absent")

