# Function to calculate change
def change(cost, payment):
    change = payment - cost
    return change

item_cost = float(input("Please enter the cost of the item: "))
payment_made = float(input("Please enter customer payment: "))
change_needed = change(item_cost, payment_made)
print("Change given: ", change_needed)
