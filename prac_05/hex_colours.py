# Adrianto Hartono
# 14347930

"""
Hex Colours
"""

COLORS = {
    "ACIDGREEN": "	##b0bf1a",
    "ALICEBLUE": "#f0f8ff",
    "AQUA": "#00ffff",
    "APRICOT": "#fbceb1",
    "BABYBLUE": "#89cff0",
    "BEIGE": "#f5f5dc",
    "BLACK": "#000000",
    "CAMEL": "#c19a6b",
    "CRYSTAL": "#a7d8de",
    "FAWN": "#e5aa70"
}

color_name = input("Enter the color name: ").upper()

while color_name != "":
    if color_name in COLORS:
        print(f"The hexadecimal color code for {color_name} is {COLORS[color_name]}")
    else:
        print(f"Sorry, your input for {color_name} is Invalid. Please try again.")
    color_name = input("Enter the color name: ").upper()

print("Bye, thank you!")