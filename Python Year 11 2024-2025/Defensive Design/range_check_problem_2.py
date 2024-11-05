quantity = int(input("Enter the quantity of products you are purchasing: "))
while quantity < 1 or quantity > 100:
    print("Invalid quantity")
    quantity = int(input("Enter the quantity of products you are purchasing: "))
print("Valid quantity entered")

total_price = 0
for i in range(quantity):
    price = float(input(f"Enter the price of product no. {i+1}: "))
    while price < 10 or price > 150:
        print("Invalid price")
        price = float(input(f"Enter the price of product no. {i+1}: "))
    total_price += price

print(f"Total quantity: {quantity}")
print(f"Total price: £{total_price}")