# What does this program do? This program performs a linear search on a set array of numbers

# Array of numbers to be searched
numbers = [5, 1, 9, 8, 7, 6, 4, 10]
# Number item input to be searched for in above array
searchItem = int(input("Enter item to be searched: "))
# For loop iterates through each item in the numbers array
for i in range(len(numbers)):
    # Checks if the array contains the number being searched for (searchItem)
    # if numbers[i] == searchItem:
    if searchItem in numbers:
        # Outputs success result of item found
        print("searchItem found")
        break # Break loop once item found
    else:
        print("searchItem not found")
# Program ends

# How can this program be improved?

# 1. Run the program
# 2. Annotate the program
# 3. Improve the program
