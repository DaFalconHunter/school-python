pin = '1977'

# userPin = ""
"""
while True:
    userPin = input("Enter your 4-digit PIN: ")

    if userPin == pin:
        print("PIN correct, you may proceed.")
        break
    else:
        print("The PIN you entered was incorrect.\nPlease try again.")
"""

"""
while pin != userPin:
    userPin = input("Enter your 4-digit PIN: ")
    if userPin == pin:
        print("PIN correct, you may proceed.")
    else:
        print("The PIN you entered was incorrect.\nPlease try again.")
"""

attempt = 0
for i in range(0, 3):
    userPin = input("Enter your 4-digit PIN: ")
    attempt += 1

    if userPin == pin:
        print("PIN correct, you may proceed.")
        break
else:
    print("You are out of attempts.")
