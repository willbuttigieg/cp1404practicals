"""
CP1404 Practical 7
Project class
"""
from datetime import datetime

class Project:
    """Represent a project object."""

    def __init__(self, name, start_date, priority, estimated_cost, completion_percentage=0):
        """Initialize a project instance."""
        self.name = name
        self.start_date = datetime.strptime(start_date, "%d/%m/%Y").date()
        self.priority = priority
        self.estimated_cost = estimated_cost
        self.completion_percentage = completion_percentage

    def __str__(self):
        """Return a string representation of the project."""
        return (f"{self.name}, start: {self.start_date.strftime("%d/%m/%Y")}, priority {self.priority}, "
                f"estimate: ${self.estimated_cost}, completion: {self.completion_percentage}%")

    def __gt__(self, other):
        return self.priority > other.priority

    def is_complete(self):
        """Return True if the project is complete."""
        return self.completion_percentage == "100"
