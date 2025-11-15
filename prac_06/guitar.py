"""
Guitar class for storing guitar details.
Estimated time: 30 minutes
Actual time:60 minutes
"""

class Guitar:
    """Represent a Guitar object"""
    def __init__(self, name="",year=0,cost=0):
        """Initialize guitar instance

        name: sting, guitar name
        year: int, year guitar was made
        cost: float, guitar cost
        """
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return string representation of Guitar."""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def get_age(self):
        """Return age of guitar"""
        current_year = 2022
        return current_year - self.year


    def is_vintage(self):
        """Determine whether vintage or not """
        return self.get_age() >= 50
