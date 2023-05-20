# Adrianto Hartono
# 14347930

from taxi import Taxi

class SilverServiceTaxi(Taxi):
    price_per_km = Taxi.price_per_km
    flagfall = 4.50

    def __init__(self, name, fuel, faciness):
        super().__init(name, fuel)
        self.price_per_km *= faciness

    def __str__(self):
        return f"{super().__str__()} plus flagfall of ${self.flagfall}:,.2f"

    def get_fare():
        return super().get_fare() + self.flagfall
