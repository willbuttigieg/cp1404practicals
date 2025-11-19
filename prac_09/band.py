class Band:
    """Band class"""

    def __init__(self, name):
        """Initialize the Band class"""
        self.name = name
        self.musicians = []

    def __repr__(self):
        """Return a string representation of a Musician."""
        return f"{self.name} ({', '.join(str(musician) for musician in self.musicians)})"

    def add(self, musician):
        """Add a musician to the musicians."""
        self.musicians.append(musician)

    def play(self):
        """List the musicians in the band and the instruments they play."""
        play_string = []
        for musician in self.musicians:
            if musician.instruments:
                play_string.append(f"{musician.name} is playing: {musician.instruments[0]}")
            else:
                play_string.append(f"{musician.name} needs an instrument!")
        return "\n".join(play_string)