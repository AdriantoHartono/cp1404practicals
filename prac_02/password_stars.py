# Adrianto Hartono
# 14347930

MINIMUM = 10

password = input("Enter Password: ")
while len(password) < MINIMUM:
    print("Your password doesn't meet the minimum length")
    password = input("Enter Password: ")

for i in range(0, len(password)):
    print("*", end="")