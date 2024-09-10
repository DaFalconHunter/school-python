forename = input("Enter forename: ")
surname = input("Enter surname: ")
userp1 = forename[:4] + surname[:4]
userp1 = userp1.lower()

for counter in range(1000,1003):
    userp2 = str(counter)
    print("Suggested username:",userp1 + userp2)

username = ""
while len(username) < 4 or len(username) > 12:
    username = input("Enter a chosen username: ")

    if len(username) < 4:
        print("Too few characters.")
    elif len(username) > 12:
        print("Too many characters.")
    else:
        print("Valid username chosen.")


