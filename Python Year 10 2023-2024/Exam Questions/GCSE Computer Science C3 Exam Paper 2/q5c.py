level = 0
code = ""
while len(code) != 3:
    code = input("Enter you 3-character code: ")
    if code == "SVA":
        level = 2
    elif code == "UTV":
        level = 3
    else:
        level = 1

print(f"You will be playing level {level}")
