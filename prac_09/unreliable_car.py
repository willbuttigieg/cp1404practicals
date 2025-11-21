"""CP1404 Practical 9 - Unreliable Car"""

from prac_09.car import Car
from random import randint


class UnreliableCar(Car):
    """Unreliable Car class with Car as it's parent class."""

    def __init__(self, name, fuel, reliability):
        """Initialize attributes of the UnreliableCar class."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive the car depending on it's reliability."""
        random_number = randint(0, 100)
        if random_number >= self.reliability:
            distance = 0
        distance_driven = super().drive(distance)
        return distance_driven
