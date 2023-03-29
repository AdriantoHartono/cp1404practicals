# Adrianto Hartono
# 14347930

import random

print(random.randint(5, 20))  # line 1
print(random.randrange(3, 10, 2))  # line 2
print(random.uniform(2.5, 5.5))  # line 3

"""
What did you see on line 1?
What was the smallest number you could have seen, what was the largest?
> The smallest number I could have seen is 5, and the largest is 19

What did you see on line 2?
What was the smallest number you could have seen, what was the largest?
Could line 2 have produced a 4?
> The smallest number that I could have seen is 3, and the largest is 9
> Line 2 could not produce 4, because the step is 2 and after 3 it should be 5, 7, and 9

What did you see on line 3?
What was the smallest number you could have seen, what was the largest?
> The smallest number I could have seen is 2.5, and the largest is 5.499999999999999
"""

# Write code, not a comment, to produce a random number between 1 and 100 inclusive.
print(random.randint(1,100))