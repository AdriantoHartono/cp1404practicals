# Adrianto Hartono
# 14347930

"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
> When we enter the wrong value from the value that assigned in an object
2. When will a ZeroDivisionError occur?
> When the number is divided by 0
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
> Yes, I can put the code to make the user cannot input 0 to run the code
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    # Program to avoid the possibility of a ZeroDivisionError
    while denominator == 0:
        print("You cannot divide it with 0")
        denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")