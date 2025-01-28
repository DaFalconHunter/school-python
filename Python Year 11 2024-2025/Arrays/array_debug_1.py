# Add a new student to the end of a list
# There are 5 syntax errors and 1 runtime error
# How would you improve the program?

students = ["Casey", "Barnaby", "Lee", "Robin"]
name = input("Name: ")
students.append(name)
for person in students:
    print(person)
