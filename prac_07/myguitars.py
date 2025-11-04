"""
CP1404 Practical 7
More Guitars!
"""

from guitar import Guitar


def main():
    """Read guitar details from file, save as objects and display them"""
    guitars = []
    in_file = open("guitars.csv", "r")
    for line in in_file:
        parts = line.strip().split(",")
        guitars.append(Guitar(parts[0], parts[1], parts[2]))
    in_file.close()
    display_guitars(guitars)
    sort_guitars(guitars)
    print()
    print("Sorted guitars:")
    display_guitars(guitars)


def display_guitars(guitars):
    """Display all guitars."""
    for guitar in guitars:
        print(guitar)


def sort_guitars(guitars):
    """Sort guitars by year."""
    guitars.sort()


main()
