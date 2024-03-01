#Question 3
#Password checker
#Password needs to be between 8 and 12 characters in length
password = input("Please enter your password")
if len(password) >= 8 and len(password) <= 12:
    print("Valid password")
else:
    print("Invalid password")
