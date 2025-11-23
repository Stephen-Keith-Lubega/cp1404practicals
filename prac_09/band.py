"""
CP1404/CP5632 Practical
Band class
"""


class Band:
    """Band class that contains musicians."""

    def __init__(self, name):
        """Initialise a Band with a name and empty list of musicians."""
        self.name = name
        self.musicians = []

    def __str__(self):
        """Return a string representation of the Band."""
        musicians_str = ", ".join(str(musician) for musician in self.musicians)
        return f"{self.name} ({musicians_str})"

    def add(self, musician):
        """Add a musician to the band."""
        self.musicians.append(musician)

    def play(self):
        """Make all musicians in the band play their first instrument."""
        for musician in self.musicians:
            # Check if musician has instruments
            if musician.instruments:
                print(f"{musician.name} is playing: {musician.instruments[0]}")
            else:
                print(f"{musician.name} needs an instrument!")