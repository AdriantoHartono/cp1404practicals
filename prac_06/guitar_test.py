# Adrianto Hartono
# 14347930

"""
Guitar Test

Expect: 15 min
Actually: 9 min
"""

from prac_06.guitar import Guitar

gibson_guitar = Guitar("Gibson L-5 CES", 1922, 16035.40)
another_guitar = Guitar("Another Guitar", 1973, 14200)

print(f"{gibson_guitar.name} get_age() - Expected 101. Got {gibson_guitar.get_age()}")
print(f"{another_guitar.name} get_age() - Expected 50. Got {another_guitar.get_age()}")
print(f"{gibson_guitar.name} is_vintage() - Expected True. Got {gibson_guitar.is_vintage()}")
print(f"{another_guitar.name} is_vintage() - Expected True. Got {another_guitar.is_vintage()}")