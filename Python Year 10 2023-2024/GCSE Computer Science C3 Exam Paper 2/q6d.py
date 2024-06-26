# Question 6d
# See the question on page 10 of the cycle 3 assessment.
# Program a solution to the problem.
# Upload your completed solution to Teams.

flxp = int(input("Enter your no. of years of flying experience: "))
miles = int(input("Enter the no. of miles you've flown today: "))
payperday = 0
paypermile = 0

if flxp < 2:
    payperday = 120
    paypermile = 0.45
elif flxp >= 2 and flxp <= 5:
    payperday = 150
    paypermile = 0.65
elif flxp > 5:
    payperday = 180
    paypermile = 0.85
    
pay = payperday + (paypermile * miles)
print(f"Your pay today is £{pay}0")