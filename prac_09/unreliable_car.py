"""
CP1404/CP5632 Practical
UnreliableCar class
"""
from random import randint
from prac_09.car import Car


class UnreliableCar(Car):
    """Specialised version of a Car that is unreliable."""

    def __init__(self, name, fuel, reliability):
        """Initialise an UnreliableCar instance, based on parent class Car."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive the car only if random number is less than reliability."""
        random_number = randint(0, 100)
        if random_number < self.reliability:
            # Car is reliable this time, drive normally
            distance_driven = super().drive(distance)
            return distance_driven
        else:
            # Car is unreliable this time, don't drive at all
            return 0