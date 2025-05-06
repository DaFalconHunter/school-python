""" Challenge 109"""
# Debug the following program.
# There are 5 syntax errors.
# Comment on the code to explain what each section is doing

# Allows the user to create a file, display the file, or add a new item to the file with user input.
print("Choose from the following options:")
print("1) Create new file")
print("2) Display the file")
print("3) Add a new item to the file")
selection = input("Make a selection 1, 2, or 3: ")

# Conduct file operations based on user selection
if selection == "1":
    file = open("Subject.txt", "w", encoding="utf-8")
    subject = input("Please enter a subject: ")
    file.write(subject)
elif selection == "2":
    file = open("Subject.txt", "r", encoding="utf-8")
    contents = file.read()
    print(contents)
elif selection == "3":
    subject = input("Please enter a new subject: ")
    file = open("Subject.txt", "r", encoding="utf-8")
    file.write(subject)
    contents = file.read()
    print(contents)
else:
    print("Sorry you didn't type in 1, 2 or 3")
