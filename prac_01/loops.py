# Adrianto Hartono
# 14347930

#3. Loops

# Display odd numbers between 1 and 20 with space between each one
for i in range(1, 21, 2):
    print(i, end=' ')
print()

# a. count in 10s from 0 to 100
for i in range(0, 101, 10):
    print(i, end=' ')
print()

# b. count down from 20 to 1
for i in range(20, 0, -1):
    print(i, end=' ')
print()

# c. print in n stars
stars = int(input("Number of stars: "))
for i in range(0, stars):
    print("*", end='')
print()

# d. print n lines of increasing stars
stars = int(input("Number of stars: "))
for i in range(1, stars+1):
    print(i * "*")
