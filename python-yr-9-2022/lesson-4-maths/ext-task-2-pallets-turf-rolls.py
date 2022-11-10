# Task E2 Turf Calculator - Pallets & Rolls (Modified with rounding)

print("Welcome to Turf Calculator!")
length = round(float(input("Please enter the length of the garden in metres: ")))
width = round(float(input("Please enter the width of the garden in metres: ")))
area = length * width
print(f'You will need {area} square metres of turf.')
pallets = area // 4
rolls = area % 4
print(f'You will need to order {pallets} pallets and {rolls} rolls of turf.')
