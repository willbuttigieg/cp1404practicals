"""
CP1404 Practical 6
Guitars

Estimated time for completion: 35 minutes
Time started: 1:31pm
Total time taken: 40 minutes
"""

class Guitar:
    """Represent a guitar object."""
    def __init__(self, name="", year=0, cost=0):
        """Initialize a guitar instance."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return a string representation of the guitar instance."""
        return f"{self.name} ({self.year}): ${self.cost:,.2f}"

    def get_age(self):
        """Return the age of the guitar."""
        return 2025 - self.year

    def is_vintage(self):
        """Return True if the guitar is considered vintage."""
        return self.get_age() >= 50