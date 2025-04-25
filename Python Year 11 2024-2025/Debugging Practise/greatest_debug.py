# De-bug the following program
# There are 4 syntax errors
# Identify the parameters

def greatest(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c

a = int(input("Please enter your first number: "))
b = int(input("Please enter your first number: "))
c = int(input("Please enter your first number: "))
print("The biggest number is: ", greatest(a, b, c))
