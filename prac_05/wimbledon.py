# Adrianto Hartono
# 14347930

"""
Game, Set, Match
Estimate: 50 minutes
Actual: 59 minutes
"""

FILENAME = "wimbledon.csv"
champions = {}
champion_country = []

def main():
    get_champion()
    display_champion()
    display_country()

def get_champion():
    with open(FILENAME, "r", encoding="utf 8-sig") as in_file:
        content = in_file.readlines()[1:]
        for word in content:
            name = word.split(",")[2]
            if name in champions:
                champions[name] += 1
            else:
                champions[name] = 1
            country_name = word.split(",")[1]

            if country_name not in champion_country:
                champion_country.append(country_name)

def display_country():
    champion_country.sort()
    print(f"These {len(champion_country)} countries have won Wimbledon: ")
    print(", ".join(champion_country))

def display_champion():
    print("Wimbledon Champions: ")
    for name in champions:
        print(f"{name}: {champions[name]}")
    print("")

main()