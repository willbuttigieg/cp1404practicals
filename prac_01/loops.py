for i in range(1, 21, 2):
    print(i, end=' ')
print()

# a.
for i in range(0, 101, 10):
    print(i, end=' ')
print()

# b.
for i in range(20, 0, -1):
    print(i, end=' ')
print()

# c.
number_of_stars_in_c = int(input("Number of stars: "))
for i in range(number_of_stars_in_c):
    print("*", end='')
print()

# d.
number_of_stars_in_d = int(input("Number of stars: "))
for i in range(1, number_of_stars_in_d + 1):
    print('*' * i)
print()
