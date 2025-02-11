length = float(input("Length: "))
width = float(input("Width: "))
carpet_type = input("Carpet type (b)asic, (s)tandard, or (l)uxury: ")
area = length * width
cost = 0
fitting = 3.75
carpet_price = 0
match carpet_type:
    case "b":
        carpet_price = 6.5
    case "s":
        carpet_price = 18.75
    case "l":
        carpet_price = 29.5

