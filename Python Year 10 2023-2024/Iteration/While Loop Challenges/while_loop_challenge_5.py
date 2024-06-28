#While loop challenge 5

#Test this code by running it then hitting the enter button.
#The code should stay in a loop until a username is entered.
#Add a line of code that displays the username entered and
#some text that says "accepted" (this message should NOT be repeated)

username = ""
while not username:
    username = str(input("Enter username: "))

print(f"Your username is: {username}")
print("Accepted")