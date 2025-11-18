from musician import Musician


class Band:
    """Band class"""

    def __init__(self, name):
        self.name = name
        self.musicians = []

    def __repr__(self):
        """Return a string representation of a Musician."""
        return f"{self.name} {[str(musician) for musician in self.musicians]})"

    def add(self, musician):
        """"""
        self.musicians.append(musician)

    def play(self):
        """"""
        for musician in self.musicians:
            musician.play()