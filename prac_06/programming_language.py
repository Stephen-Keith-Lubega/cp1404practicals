"""
CP1404/CP5632 Practical - programming language class.
Estimated time: 30 minutes
Actual time: 60 minutes
"""


class ProgrammingLanguage:
    """Represent a Programming Language."""

    def __init__(self, name, typing, reflection, year):
        """Create a programming language."""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """Check if language is dynamically typed."""
        return self.typing == "Dynamic"

    def __str__(self):
        """Return string representation."""
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"