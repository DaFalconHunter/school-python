# Question 1

print("What is your first name?")
firstname = input()
print("Hello,", firstname)
print("What is your surname?")
surname = input()
# Question 2
# print("Your surname is,", surname)

# Question 3
# print("Hello,",firstname, surname)

# Question 4
# print("Your initials are:", firstname[0], surname[0])

# Question 5
# fullname = firstname + " " + surname
# print(fullname)

# Question 6
# print(firstname.upper())

# Question 7
# firstname_length = len(firstname)
# print("Your first name is " + str(firstname_length) + " characters long")

# Question 8
username = surname[0:3] + firstname[0] + str(len(firstname))
print("This is your username: ", username)
