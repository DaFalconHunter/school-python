# Input the password:
password = input("Enter password: ")

# Check that while the password is not equal to the required password, ask the user to enter it again:
while password != "password123":
    password = input("Enter password again: ")

# Print success message
print("Password Correct")
print("You're logged in")