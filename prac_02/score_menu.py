# Adrianto Hartono
# 14347930

MENU ="""(G)et a valid score
(P)rint result
(S)how stars
(Q)uit"""

def main():
    score = 0
    print(MENU)
    answer = input(">>> ").upper()
    while answer != "Q":
        if answer == "G":
            score = get_valid_score("Enter score: ", 0, 100)
            print(f"Your score : {score}")
        elif answer == "P":
            print(f"Your score: {score}")
            result = determine_score(score)
            print(f"Result    : {result}")
        elif answer == "S":
            print(f"Your score is {score}, and here is your star: ")
            for i in range(score):
                print("*", end="")
            print()
        else:
            print("Invalid Option")
        print()
        print(MENU)
        answer = input(">>> ").upper()
    print("Farewell")

def get_valid_score(prompt, low, high):
    """Getting valid score based on the criteria"""
    "Getting a valid score"
    score = int(input(prompt))
    while score < low or score > high:
        print("Invalid score")
        score = int(input(prompt))
    return score

def determine_score(score):
    "Determining score criteria based on the score"
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"

main()