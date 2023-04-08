# Adrianto Hartono
# 14347930

numbers = []
usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']

def main():
    # Getting number
    getting_number()
    print(f"The first number is {numbers[0]}")
    print(f"The last number is {numbers[-1]} ")
    print(f"The smallest number is {min(numbers)}")
    print(f"The largest number is {max(numbers)}")
    print(f"The average of the number is {sum(numbers)/len(numbers)}")

    print()

    # Getting Username
    getting_username()
    print(determine_answer())

def getting_number():
    for i in range(0, 5):
        number = int(input("Number: "))
        numbers.append(number)

def getting_username():
    global username
    username = input("Enter your username: ")

def determine_answer():
    if username in usernames:
        return "Access granted"
    else:
        return "Access denied"

main()