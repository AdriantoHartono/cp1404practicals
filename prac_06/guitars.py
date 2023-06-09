# Adrianto Hartono
# 14347930

"""
Guitars

Expect: 40 min
Actually: 32 min
"""

from prac_06.guitar import Guitar

def main():
    guitars = []
    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

    print("My guitars!")
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitar = Guitar(name, year, cost)
        guitars.append(guitar)
        print(guitar, "added.\n")
        name = input("Name: ")

    length = determine_longest_length(guitars)

    print("\n ... snip ... \n")
    print("These are my guitars:")
    for i, guitar in enumerate(guitars, 1):
        if guitar.is_vintage():
            vintage_string = "(vintage)"
        else:
            vintage_string= ""
        print(f"Guitar {i}: {guitar.name:>{length}} {(guitar.year)}, worth ${guitar.cost:10,.2f}{vintage_string}")

def determine_longest_length(guitars):
    length = 0
    for guitar in guitars:
        if len(guitar.name) > length:
            length = len(guitar.name)
    return length

main()