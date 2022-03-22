"""
input item price
input quantity purchased
total spend = item price * quantity purchased
if total spend > 50 then
    discount = 10% of total spend
    print “you are eligible for a 10% discount at ” + discount
    amount to pay = total spend - discount
    print “this is the amount to pay: ” + amount to pay
else
    print amount to pay
endif
"""

item_price = float(input('Item Price: '))
quantity = int(input('Quantity: '))
total = item_price * quantity
if total > 50:
    discount = total * 0.1
    print("You are eligible for a 10% discount at " + discount)
    amount_due 