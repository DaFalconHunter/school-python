#Create a list of numbers

numbers = []
more_numbers = True
while more_numbers == True:
    new_number = int(input("Number: "))
    numbers.append(new_number)
    more = input("Do you want to add another number? (y/n) ")
    if more == "n":
        more_numbers = False
        
print(numbers)
