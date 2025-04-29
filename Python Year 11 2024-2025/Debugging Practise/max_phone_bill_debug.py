# Sara is writing a program to input her monthly phone bills
# and output the month name and amount for each month along
# with the month that had the maximum cost.

# De-bug the program, there are 4 syntax errors and 1 logic error.

monthName = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]
phoneBill = [0] * 12
print(phoneBill)
maxPhoneBill = 0
maxMonth = ""

for m in range(0, 12):
    print("Please input phone bill for month " + monthName[m])
    phoneBill[m] = float(input())
    if phoneBill[m] > maxPhoneBill:
        maxPhoneBill = phoneBill[m]
        maxMonth = monthName[m]

print("Maximum Phone Bill: " + maxMonth + " for " + str(maxPhoneBill))
input("\nPress ENTER to exit program ")
