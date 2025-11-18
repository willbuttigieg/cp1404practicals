"""CP1404 Prac 9 SilverServiceTaxi Program"""

from taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Silver Service Taxi Class"""
    flagfall = 4.50

    def __init__(self, name='', fuel=0, fanciness=1):
        """Initialise a Silver Service Taxi object."""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km = Taxi.price_per_km * fanciness

    def __str__(self):
        """Return a string representation of the silver service taxi."""
        return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}"

    def get_fare(self):
        """Return the price of the taxi trip including flagfall and fanciness factor."""
        return self.price_per_km * self.current_fare_distance + self.flagfall
