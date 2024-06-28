# Leap year program

# -------------------------
# Subprograms
# -------------------------
def is_leap_year(year_input):
    if year_input % 400 == 0:
        return True
    elif year_input % 100 == 0:
        return False
    elif year_input % 4 == 0:
        return True

# -------------------------
# Main program
# -------------------------
year = int(input("Enter the year: "))
if is_leap_year(year):
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")
