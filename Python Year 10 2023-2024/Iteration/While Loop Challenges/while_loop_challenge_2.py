#While loop challenge 2

#Rearrange the four lines of code below.
#to get the while loop to work.
#It should keep asking "are we there yet" until "y" entered
#You might need to indent some lines

answer = "N"
while answer != "Y":
    print("Are we there yet?")
    answer = str(input("Please respond, y or n: ").upper())
print("Yay! We are there!!")
