# Task E1 Turf Calculator (Modified with rounding)

print("Welcome to Turf Calculator!")
length = round(float(input("Please enter the length of the garden in metres: ")))
width = round(float(input("Please enter the width of the garden in metres: ")))
area = length * width
print(f'You will need {area} square metres of turf.')
