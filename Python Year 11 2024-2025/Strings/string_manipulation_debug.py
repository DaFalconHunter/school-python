#Output initial and surname
#De-bug the following program and follow the instructions

firstName = input("Enter your first name: ")
surname = input("Enter your surname: ")

#What do you add at the end of this line to extract
#the first character from the first name?
initial = firstName[0]
    
#What do you add after the . to make sure the initial is uppercase?
initialUpper = initial.upper()

surnameStart = surname[0]
surnameStart = surnameStart.upper()

# What do you need to add at the beginning of the surname
#to find the length of the variable?
length = len(surname)
remain = surname[1:]

lowerRemain = remain.lower()

#What is the technique being used here to make sure the variables are strings?
#ANSWER: Casting
surname = str(surnameStart) + str(lowerRemain)

#What is the technique being used here to join two variables together?
#ANSWER: String concatenation
fullName = initialUpper + " " + surname
print(fullName)

#What is the purpose of the \n
#ANSWER: To create a new line
input("\nPress ENTER to exit program ")
