"""
CP1404 Practical 3
Files
"""
# 1.
name = input("What is your name? ")
out_file = open("name.txt", "w")
print(name, file=out_file)
out_file.close()

# 2.
in_file = open("name.txt", "r")
name = in_file.read().strip()
in_file.close()
print(f"Hi {name}!")

# 3.
with open("numbers.txt", "r") as in_file:
    numbers = in_file.readlines()
    total = int(numbers[0].strip()) + int(numbers[1].strip())
print(total)

# 4.
total = 0
with open("numbers.txt", "r") as in_file:
    for line in in_file:
        total += int(line.strip())
print(total)