password = ""
password_2 = "1"
while password != password_2:
    password = input("Enter password: ")
    while len(password) < 8 or len(password) > 15:
        print("Invalid password")
        password = input("Enter password: ")
    print("Valid password")
    password_2 = input("Enter password again: ")
    print("Passwords were not the same. Try again")
