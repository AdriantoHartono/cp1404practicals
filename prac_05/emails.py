# Adrianto Hartono
# 14347930

"""
Emails
Estimate: 30 minutes
Actual: 37 minutes
"""

users = {}

user_input = input("Email: ")

while user_input != "":
    name = user_input.split('@')[0]
    name = ' '.join(name.split('.')).title()
    confirmation = input(f"Is your name {name}? (Y/n) ").lower()
    if confirmation != "y" and confirmation != "":
        name = input("Name: ").title()
    users[user_input] = name
    user_input = input("Email: ")

print()

for email, name in users.items():
    print(f"{name} ({email})")
