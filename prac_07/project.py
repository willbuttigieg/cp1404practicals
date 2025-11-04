"""
CP1404 Practical 7
Project class
"""


class Project:
    """Represent a project object."""

    def __init__(self, name, start_date, priority, estimated_cost, completion_percentage):
        """Initialize a project instance."""
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.estimated_cost = estimated_cost
        self.completion_percentage = completion_percentage

    def __str__(self):
        """Return a string representation of the project."""
        return (f"{self.name}, start: {self.start_date}, priority {self.priority}, estimate: ${self.estimated_cost}, "
                f"completion: {self.completion_percentage}%")
