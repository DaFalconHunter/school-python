head_circum = int(input("Head circumference: "))
if head_circum > 40:
    print("Hat size is too big - large")
elif head_circum < 25:
    print("Hat size is too small - small")
else:
    print("This hat size is medium")