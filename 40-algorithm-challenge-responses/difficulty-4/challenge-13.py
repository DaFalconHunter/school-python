"""
Challenge 13:

A company calculates holiday allowance for employees.

The company gives each employees 28 days holiday each year. Holidays are awarded based on the following rules:

1. Full time employees who work 5 days a week get 28 days holiday a year

2. Part time employees get a proportion of holiday allowance based on how many days they work, e.g. An employee who works 1 day a week would only get 1/5th of the holidays allowed.
"""
import math

# Retrieve employee details:

# Full time or part time?
emp_type = input('Full time (f) or part time (p)? ')

if emp_type == 'f':
    print("As a full time employee who works 5 days a week, you'll be allowed 28 days of holiday a year.")
else:
    pt_emp_work_days = int(input('Please enter the no. of days you work per year: '))
    pt_emp_work_holidays = math.floor(pt_emp_work_days / 5)
    print(f"As a part time employee who works {pt_emp_work_days} days per year, your allowance of holidays will be {pt_emp_work_holidays} days.")

