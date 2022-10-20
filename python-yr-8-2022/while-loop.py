# Input the password:
password = input("Enter password: ")
count = 0

# Check that while the password is not equal to the required password, ask the user to enter it again:
while count != 3:
    count += 1
    if password == "password123":
        print("Welcome, you are logged in.")
        print("It took you " + str(count) + " times to login. Next time remember your password.")
        count = 3
    else:
        print("This was attempt number " + str(count))
        password = input("Try again: ")
