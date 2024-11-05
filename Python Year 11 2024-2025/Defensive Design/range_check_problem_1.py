age = int(input("Please enter age: "))
while age < 16 or age > 19:
    print("Age invalid")
    age = int(input("Please enter age: "))
print("Age valid")