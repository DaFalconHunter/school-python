#For loop challenge 3

#The code below is mixed up
#It should ask the user to enter their name.
#It should then display the name twice
#If possible, upgrade the code to...
#ask the user how many times they want...
#their name to be displayed

name = str(input("Input your name>>>"))
times = int(input("How many times do you want your name displayed? "))
for i in range(times):
    print(name)
