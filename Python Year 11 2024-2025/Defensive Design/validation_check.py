# PRESENCE CHECK:

# With selection statements:
# name = input("Please enter name: ")
# if name == "":
#     print("No data entered")
# else:
#     print("Thank you for entering your name")

# With iteration:
# name = input("Please enter name: ")
# while name == "":
#     print("No data entered")
#     name = input("Please enter name: ")
# print("Thank you for entering your name")

# LENGTH CHECK:

# With selection statements:
# postcode = input("Please enter postcode: ")
# if len(postcode) < 6 or len(postcode) > 8:
#     print("Invalid postcode")

# With iteration:
postcode = input("Please enter postcode: ")
while (len(postcode) < 6 or len(postcode) > 8) and postcode == "":
    print("Invalid postcode")
    postcode = input("Please enter postcode: ")
print("Valid postcode")