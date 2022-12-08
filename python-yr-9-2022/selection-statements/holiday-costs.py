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
party_num = num_children + num_adults

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
total_holiday_cost = (
    total_adults_flight_cost
    + total_child_flight_cost
    + total_adults_accom_cost
    + total_child_accom_cost
)

# 3. - Final Discounts
# - 💷 > £1000: => -1%🔻
# - 💷 > £2000: => -2%🔻
# - 💷 > £5000: => -7%🔻

holiday_7_bool = False
holiday_2_bool = False
holiday_1_bool = False

if total_holiday_cost > 5000:
    holiday_disc = total_holiday_cost * 0.93
    holiday_7_bool = True
elif total_holiday_cost > 2000:
    holiday_disc = total_holiday_cost * 0.98
    holiday_2_bool = True
elif total_holiday_cost > 1000:
    holiday_disc = total_holiday_cost * 0.99
    holiday_1_bool = True
else:
    holiday_disc = total_holiday_cost

# 2. b)
# - If party no. > 5: => -10%🔻 on full price:
if party_num > 5:
    holiday_10 = round(total_holiday_cost * 0.9, 2)
else:
    holiday_10 = holiday_disc

holiday_10_bool = 0
if holiday_10 != total_holiday_cost:
    holiday_10_bool = True
else:
    holiday_10_bool = False

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

Cost of flights: £{total_flight_cost}
Cost of accommodation: £{total_acccom_cost}
Total holiday cost: £{total_holiday_cost}

Discounts & deductions:
 - Free child place incl. (True/False): {free_child_bool}
 - 10% discount for travelling in a group of > 5: {holiday_10_bool}
 - Total holiday cost > £1000: => -1%🔻: {holiday_1_bool}
 - Total holiday cost > £2000: => -2%🔻: {holiday_2_bool}
 - Total holiday cost > £5000: => -7%🔻: {holiday_7_bool}

Final holiday costs: £{holiday_10}

Enjoy your holiday!
**************************************************
""".format(
    country=country,
    destination=destination,
    num_adults=num_adults,
    num_children=num_children,
    free_child_bool=free_child_bool,
    holiday_10_bool=holiday_10_bool,
    holiday_10=holiday_10,
    holiday_1_bool=holiday_1_bool,
    holiday_2_bool=holiday_2_bool,
    holiday_7_bool=holiday_7_bool,
    total_flight_cost=total_flight_cost,
    total_acccom_cost=total_acccom_cost,
    total_holiday_cost=total_holiday_cost,
)

print(holiday_summary)
