#Question 2
#De-bug the program and test to make sure it is working.

length = int(input("Enter a base length"))
height = int(input("Enter a height"))
if length < 20:
    area = (length * height) / 2
    print(area)
else:
    print("Base length is too long.")

