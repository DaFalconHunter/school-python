# While loop challenge 10

# Write some code that repeatedly asks you..
# "What coding language is this?"..
# and displays "ok, thanks!" when you type in "Python"

answer = ""
while answer != "python":
    answer = input("What coding language is this? ").lower()

print("Ok, thanks!")
