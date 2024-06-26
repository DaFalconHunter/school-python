# Year 10 Cycle 3 - Question 4.
# 1. De-bug the following code to get it working.
# 2. State the output if the name Devveena Thulsie was entered.
# 3. Add a line of code to ask for the users year of birth.
# 4. Amend the userName to include the year of birth.
# Upload your completed solution to Teams.

first = input("Enter your first name: ")
second = input("Enter your second name: ")
age = input("Enter your bith year: ")
userOne = first[0:2]
userTwo = second[0:3]
userName=userOne+userTwo+age
print("Your username is: ", userName)
