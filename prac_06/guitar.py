# Adrianto Hartono
# 14347930

"""
Guitar

Expect: 20 min
Actually: 14 min
"""

class Guitar:
    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def get_age(self):
        return 2023 - self.year

    def is_vintage(self):
        if self.get_age() >= 50:
            return True
        else:
            return False

    def __lt__(self, other):
        return self.year < other.year