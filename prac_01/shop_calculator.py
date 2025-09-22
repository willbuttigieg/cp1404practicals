"""
Shop Calculator
Takes the number of items and price of each item from user and calculates total
"""

total_price = 0

number_of_items = int(input("Number of items: "))
while number_of_items < 0:
    print("Invalid number of items!")
    number_of_items = int(input("Number of items: "))
for i in range(number_of_items):
    price = float(input("Price of item: "))
    total_price += price
if total_price > 100:
    total_price = total_price - (total_price * 0.1)
print(f"Total price for {number_of_items} items is ${total_price:.2f}")