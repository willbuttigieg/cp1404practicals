"""
CP1404 Practical 6
Programming Language
Estimated time for completion: 25 minutes
Time started: 1pm
Total time taken: 23 minutes
"""

class ProgrammingLanguage:
    """Represent a programming language."""
    def __init__(self, name, typing, reflection, year):
        """Initialize an empty programming language."""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """Determine if this programming language is dynamic."""
        if self.typing == "Dynamic":
            return True
        else:
            return False

    def __str__(self):
        """Return a string representation of the programming language."""
        return f"{self.name}, {self.typing} typing, Reflection={self.reflection}, First appeared in {self.year}"