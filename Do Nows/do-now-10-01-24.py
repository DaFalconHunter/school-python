while True:
    light = input("Enter traffic light colour: (g)reen, (a)mber or (r)ed: ").lower()
    if light == "g":
        print("Go")
        break
    elif light == "a":
        print("Get ready")
        break
    elif light == "r":
        print("Stop")
        break
    else:
        print("Please enter the correct input: g, a or r")
