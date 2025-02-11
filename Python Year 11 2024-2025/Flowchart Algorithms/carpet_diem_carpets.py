length = float(input("Length: "))
width = float(input("Width: "))
carpet_type = input("Carpet type (b)asic, (s)tandard, or (l)uxury: ")

# Validate inputs
if length <= 0 or width <= 0:
    print("Length and width must be positive numbers.")
    exit(1)

if carpet_type not in ["b", "s", "l"]:
    print("Invalid carpet type. Please enter 'b', 's', or 'l'.")
    exit(1)

area = length * width
fitting = 3.75
carpet_price = 0

match carpet_type:
    case "b":
        carpet_price = 6.5
    case "s":
        carpet_price = 18.75
    case "l":
        carpet_price = 29.5

cost = area * carpet_price + fitting
print(f"The total cost is: ${cost:.2f}")