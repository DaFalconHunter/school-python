# Name and food program

first_name = input("Enter first name: ").title()
fav_food = input("Enter your favourite food: ").title()
food_string = first_name + " likes " + fav_food
print(food_string.upper())
print("The sentence contains " + str(len(food_string)) + " characters")