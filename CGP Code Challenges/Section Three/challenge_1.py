import math

line_dist = int(input("Enter the straight line distance in miles between points A and B: "))
line_dist_km = line_dist * 1.6
flight_path_dist = round((line_dist_km * math.pi) / 2)
print("The distance between points A and B in km along the flight path is: ", str(flight_path_dist) + "km")