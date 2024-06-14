while True:
    age = int(input("Enter your age: "))
    has_card = input("Do you have a loyalty card?(y/n): ").lower()
    if (age < 17 or age > 69) or has_card == "y":
        print("Entitled to discount")
    else:
        print("Not entitled to discount")
    again = input("Do you want to re-enter your details? (y/n): ").lower()
    if again == "y":
        continue
    else:
        break
