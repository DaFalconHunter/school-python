num_people = 0
while True:
    height = int(input("Enter your height in cm: "))
    if height >= 140:
        print("You are permitted to ride.")
        num_people += 1
    elif height >= 120:
        is_adult = input("Are you riding with an adult? (y/n): ").lower()
        if is_adult == "y":
            print("You are permitted to ride.")
            num_people += 1
        elif is_adult == "n":
            print("You are not permitted to ride.")
        else:
            print("Invalid input.")
    else:
        print("You are not permitted to ride.")
    
    if num_people == 8:
        break

