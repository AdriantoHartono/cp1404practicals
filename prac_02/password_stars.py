# Adrianto Hartono
# 14347930

MINIMUM = 10

def main():
    password = get_password()
    for i in range(0, len(password)):
        print("*", end="")
def get_password():
    """Getting password as required"""
    password = input("Enter Password: ")
    while len(password) < MINIMUM:
        print("Your password doesn't meet the minimum length")
        password = input("Enter Password: ")
    return password

main()