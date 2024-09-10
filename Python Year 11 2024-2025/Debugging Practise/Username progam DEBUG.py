forename = input("Enter forename: ")
surname = input("Enter surname: ")

# Concatenates the first 4 characters of forename and surname together
userp1 = forename[:4] + surname[:4]
userp1 = userp1.lower()

# Loop iterates from 1000 to 1002, incrementing by 1 on each iteration, and uses that number as an attachment to the auto-generated username
for counter in range(1000,1003):
    userp2 = str(counter)
    print("Suggested username:",userp1 + userp2)

username = ""
# Loops so longs as the entered username is less than 4 chars or greater than 12 chars in length
while len(username) < 4 or len(username) > 12:
    username = input("Enter a chosen username: ")

    if len(username) < 4:
        print("Too few characters.")
    elif len(username) > 12:
        print("Too many characters.")
    else:
        print("Valid username chosen.")


