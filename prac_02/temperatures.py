# Adrianto Hartono
# 14347930

MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""

def main():
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            fahrenheit = celsius_to_fahrenheit()
            print(f"Result : {fahrenheit:.2f} F")
        elif choice == "F":
            celsius = fahrenheit_to_celsius()
            print (f"Result: {celsius:.2f} C")
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")

def celsius_to_fahrenheit():
    """Calculating celsius to fahrenheit"""
    celsius = float(input("Celsius: "))
    return celsius * 9.0 / 5 + 32

def fahrenheit_to_celsius():
    """Calculating fahrenheit to celsius"""
    fahrenheit = float(input("Fahrenheit: "))
    return 5 / 9.0 * (fahrenheit - 32)

main()