# Adrianto Hartono
# 14347930

import random

def main():
    score = float(input("Enter score: "))
    result = determine_score(score)
    print(result)
    random_score = random.randint(1,100)
    result = determine_score(random_score)
    print(f"The random score: {random_score} \n{result}")

def determine_score(prompt):
    """Determining score based on the criteria"""
    if prompt < 0 or prompt > 100:
        return("Invalid score")
    elif prompt >= 90:
        return("Excellent")
    elif prompt >= 50:
        return("Passable")
    else:
        return("Bad")

main()