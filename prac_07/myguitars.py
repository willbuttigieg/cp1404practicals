"""
CP1404 Practical 7
More Guitars!
"""

from guitar import Guitar


def main():
    """Read guitar details from file, save as objects and display them"""
    guitars = read_guitars()
    sort_guitars(guitars)
    display_guitars(guitars)
    add_guitar(guitars)
    sort_guitars(guitars)
    display_guitars(guitars)
    save_guitars(guitars)


def read_guitars():
    guitars = []
    in_file = open("guitars.csv", "r")
    for line in in_file:
        parts = line.strip().split(",")
        guitars.append(Guitar(parts[0], parts[1], parts[2]))
    in_file.close()
    return guitars


def display_guitars(guitars):
    """Display all guitars."""
    for guitar in guitars:
        print(guitar)


def sort_guitars(guitars):
    """Sort guitars by year."""
    guitars.sort()


def add_guitar(guitars):
    """Add a guitar to the list of guitars."""
    name = input("Name: ")
    while name != "":
        year = input("Year: ")
        cost = float(input("Cost: $"))
        new_guitar = Guitar(name, year, cost)
        print(f"{new_guitar} added.")
        guitars.append(new_guitar)
        name = input("Name: ")


def save_guitars(guitars):
    """Save the list of guitars to file."""
    with open("guitars.csv", "w") as file:
        for guitar in guitars:
            print(f"{guitar.name},{guitar.year},{guitar.cost}", file=file)


main()
