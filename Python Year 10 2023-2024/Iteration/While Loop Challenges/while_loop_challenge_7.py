# While loop challenge7

# Please see below the following code
# that displays a times table of your choice
# Test it now.

number = int(input("Enter a times table: "))
for i in range(1, 13):
    print(i, "x", number, "=", i * number)
print("showing the", number, "times table")

# The above code uses a count based loop
# Below, attempt the same code, but
# use a condition based (while) loop
# Some of the unfinished/error code is shown below
# Be sure to debug/fix any errors
# Ready? delete the """ and put a #(comment out) on the lines of
# code above to fix the code below.

timesTable = 1
UserChoice = int(input("Enter a times-table: "))
while timesTable < 13:
    print(f"{timesTable} x {UserChoice} = {timesTable * UserChoice}")
    timesTable += 1
print("showing the", UserChoice, "times table")
