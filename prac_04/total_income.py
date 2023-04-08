# Adrianto Hartono
# 14347930

"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""


def main():
    """Display income report for incomes over a given number of months."""
    incomes = []
    number_of_month = int(input("How many months? "))

    getting_income(incomes, number_of_month)

    print("\nIncome Report\n-------------")
    total = 0
    print_income_report(incomes, number_of_month, total)

def getting_income(incomes, number_of_month):
    for number_of_month in range(1, number_of_month + 1):
        income = float(input(f"Enter income for month {str(number_of_month)}: "))
        incomes.append(income)
    return number_of_month

def print_income_report(incomes, number_of_month, total):
    for number_of_month in range(1, number_of_month + 1):
        income = incomes[number_of_month - 1]
        total += income
        print("Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(number_of_month, income, total))

main()