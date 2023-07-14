num_stars = int(input("Enter the no. of stars films will be rated with: "))
for row in range(num_stars):
    for star in range(num_stars):
        print("*" * num_stars)
        num_stars -= 1
