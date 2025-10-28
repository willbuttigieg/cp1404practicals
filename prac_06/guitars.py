"""
CP1404 Practical 6
Guitars Program

Estimated time for completion: 30 minutes
Time started: 2:33pm
Total time taken: 50 minutes
"""

from guitar import Guitar

guitars = []

# Sample data:
# guitars.append(Guitar("Fender Stratocaster", 2014, 765.40))
# guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
# guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

print("My guitars!")
name = input("Name: ")
while name != "":
    year = int(input("Year: "))
    cost = int(input("Cost: $"))
    new_guitar = Guitar(name, year, cost)
    print(f"{new_guitar} added.")
    guitars.append(new_guitar)
    name = input("Name: ")
print("These are my guitars:")
for i, guitar in enumerate(guitars):
    vintage_string = " (vintage)" if guitar.is_vintage() else ""
    print(f"Guitar {i + 1}: {guitar.name:>{max(len(guitar.name) for guitar in guitars)}} "
          f"({guitar.year}), worth ${guitar.cost:>10,.2f} {vintage_string}")
