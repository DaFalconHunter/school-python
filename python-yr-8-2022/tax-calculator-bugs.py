# L4 WS4 Tax CalculatorBUGS.py
# Tax Calculator program  with 5 bugs
# CHALLENGE: Now, calculate remaining salary after tax at the end of the year and each month.

salary = int(input("Please enter your annual salary: £"))

if salary < 30000:
    # Salaries under 30000 are taxed at 20%
    tax = salary * 0.2
elif salary >= 30000:
    # Salaries over 30000 are taxed at 40% for anything over 30000
    salary -= 30000
    tax = salary * 0.4 + 6000
else:
    # Salaries over 150000 are taxed at 45% for anything over 150000
    salary = salary - 150000
    tax = salary * 0.45 + 6400 + 48000

print("Earnings of £", salary, "will attract taxes of £", round(tax, 2), "and leave you with a remaining salary of", salary - tax)
# Salary at the end of the year:


input("Press ENTER to quit")