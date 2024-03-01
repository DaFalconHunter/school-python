is_student = input("Are you a student? (y/n): ").lower().strip() == "y"
has_discount_card = input("Do you have a discount card? (y/n): ").lower().strip() == "y"
is_saturday = input("Is it Saturday today? (y/n): ").lower().strip() == "y"

if (is_student or has_discount_card) and not is_saturday:
    print("You will have 50% off")
else:
    print("You will not have 50% off")
