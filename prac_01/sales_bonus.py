# Adrianto Hartono
# 14347930

# 1. Sales Bonus

"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,0000 or over, the bonus is 15%
"""

"""
get sales
while sales >= 0
    if sales < 1000
        bonus = sales * 0.10
        display bonus
    else
        bonus = sales * 0.15
        display bonus
    get sales    
"""

sales = float(input("Enter sales: $"))
while sales >= 0:
    if sales < 1000:
        bonus = sales * 0.10  #10%
        print(f"Your bonus is ${bonus:.0f}")
    else:
        bonus = sales * 0.15  #15%
        print(f"Your bonus is ${bonus:.0f}")
    sales = float(input("Enter sales: $"))




