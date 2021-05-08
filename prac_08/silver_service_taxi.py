from prac_08.taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Fixed initial surcharge."""
    flagfall = 4.5

    def __init__(self, name, fuel, fanciness):
        """Initialise a Silver Service Taxi instance, based on parent class Taxi."""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km += fanciness

    def __str__(self):
        """Return a string with a Taxi and flagfall"""
        return "{} plus flagfall of ${:.2f}".format(super().__str__(), self.flagfall)

    def get_fare(self):
        """Returns price for the Taxi trip"""
        return self.flagfall + super().get_fare()
