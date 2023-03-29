# Adrianto Hartono
# 14347930

# Question 1
out_file = open('name.txt', 'w')
name = input("Enter your name: ")
print(name, file=out_file)
out_file.close()

# Question 2
out_file = open('name.txt', 'r')
name = out_file.read()
print(f"Your name is {name}")

# Question 3
out_file = open('numbers.txt', 'r')
result = 0
out_file = open('numbers.txt', 'r')
for i in range(0, 2):
    number = out_file.readline()
    result += int(number)
print(f"The result from the first 2 numbers is {result}")
out_file.close()

# Question 4
total = 0
out_file = open('numbers.txt', 'r')
is_finished = False
while not is_finished:
    try:
        number = out_file.readline()
        total += int(number)
    except ValueError:
        is_finished = True
print(f"The total numbers from all lines is {total}")