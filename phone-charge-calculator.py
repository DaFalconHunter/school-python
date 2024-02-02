monthly_tariff = 23.00
per_min_rate = 0.02
total_charge = monthly_tariff
mins_used = int(input("Enter the no. of minutes used: "))
if mins_used > 600:
    extra_mins = mins_used - 600
    extra_charge = extra_mins * per_min_rate
    total_charge += extra_charge
print(f"£{total_charge}")