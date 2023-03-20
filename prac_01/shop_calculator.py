# Adrianto Hartono
# 14347930

# Shop Calculator
"""
total = 0
get number of items
while numbers of items < 0
    display error message
    get number of items
for i in range number of items
    get price
    total = total + price
if total > 100
    total = total - (total * 0.10)
display number of items, total
"""

total = 0
numbers = int(input("Number of items: "))
while numbers < 0:
    print("Invalid number of items!")
    numbers = int(input("Number of items: "))
for i in range(0, numbers):
    price = float(input(f"Price of item: "))
    total += price
if total > 100:
    total = total - (total * 0.10) #10%
print(f"Total price for {numbers} items is ${total:.2f}")
