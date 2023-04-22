"""
Challenge 23:

Create an algorithm that will:

· Allow the user to input how much money they want to change to coins.

· Select which coin they want to convert the money into £1, 50p, 20p, 10p, 5p, 2p ,1p

· Calculate how many of each coin will be given in.
"""
import math

money = float(input("How much money do you want to change? £"))
coin = float(input("Select a coin to convert to: £1 (1), 50p (0.5), 20p (0.2), 10p (0.1), 5p (0.05), 2p (0.02) or 1p (0.01): "))

change = math.floor(money / coin)
print(change)
