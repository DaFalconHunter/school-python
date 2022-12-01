# COMMENT YOUR CODE WELL!

# 1. a)
# - Ask user to enter the country and destination:
country = input("What country do you want to visit? ")
destination = input("What is your destination? ")

# - Request cost of flights and accommodation:
adult_flight_cost = int(input("How much does 1 adult flight cost? "))
adult_accom_cost = int(input("How much does 1 adult accommodation cost? "))

# 1. b)
# - Ask how many children and adults are travelling:
num_children = int(input("How many children are travelling with you? "))
num_adults = int(input("And how many adults? "))

# 2. a)
# - Free child place
n_child_free = num_children - 1
if n_child_free != num_children:
    free_child_bool = True
else:
    free_child_bool = False
# 1. c)
# - Calculate flight costs for the whole party:

#   - Sum all adults flight costs:
total_adults_flight_cost = adult_flight_cost * num_adults

#   - Set 1 child's flight cost:
child_flight_cost = adult_flight_cost / 2
#   - Sum all children flight costs:
total_child_flight_cost = child_flight_cost * n_child_free

#   - Sum flights cost:
total_flight_cost = round(total_adults_flight_cost + total_child_flight_cost, 2)

# 1. d)
# - Calculate accommodation costs for the whole party:

#   - Sum all adults accommodation costs:
total_adults_accom_cost = adult_accom_cost * num_adults

#   - Set 1 child's accommodation cost:
child_accom_cost = adult_accom_cost / 2
#   - Sum all children accommodation costs:
total_child_accom_cost = child_accom_cost * n_child_free

#   - Sum accommodation cost:
total_acccom_cost = round(total_adults_accom_cost + total_child_accom_cost, 2)

# 1. e)
# - Calculate total holiday cost:
total_holiday_cost = total_adults_flight_cost + total_child_flight_cost + total_adults_accom_cost + total_child_accom_cost

# 1. f)
# - Print summary of all holiday details: 
#   - Country ✔
#   - Destination ✔
#   - No. of adults ✔
#   - No. of children ✔
#   - Flights cost ✔
#   - Accommodation cost ✔
#   - Total holiday cost ✔

holiday_summary = """\
**************************************************
This is your holiday costs summary:

Country you are visiting: {country}
Destination you are headed to: {destination}
No. of adults travelling: {num_adults}
No. of children travelling: {num_children}

Discounts & deductions:
 - Free child place incl. (True/False): {free_child_bool}

Cost of flights: £{total_flight_cost}
Cost of accommodation: £{total_acccom_cost}
Total holiday cost: £{total_holiday_cost}

Enjoy your holiday!
**************************************************
""".format(
    country=country,
    destination=destination,
    num_adults=num_adults,
    num_children=num_children,
    free_child_bool=free_child_bool,
    total_flight_cost=total_flight_cost,
    total_acccom_cost=total_acccom_cost,
    total_holiday_cost=total_holiday_cost
)

print(holiday_summary)
