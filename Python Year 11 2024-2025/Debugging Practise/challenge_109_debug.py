#Challenge 109
#Debug the following program.
#There are 5 syntax errors.
#Comment on the code to explain what each section is doing

print("Choose from the following options:")
print("1) Create new file")
print("2) Display the file")
print("3) Add a new item to the file"
selection=input("Make a selection 1, 2, or 3: ")

if seletion=="1":
    file=opn("Subject.txt","w")
    subject=input("Please enter a subject: ")
    file.write(subject)
elif selection="2":
    file=open("Subject.txt","r")
    contents=file.read()
    print(contents)
elif selection=="3":
    subject=input("Please enter a new subject: ")
    file.wrte(subject)
    file=open("Subject.txt","r")
    contents=file.read
    print(contents)
else:
    print("Sorry you didn't type in 1, 2 or 3")
