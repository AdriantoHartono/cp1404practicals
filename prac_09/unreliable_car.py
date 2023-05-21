# Adrianto Hartono
# 14347930

from prac_06.car import Car
import random

class UnreliableCar(Car):
    def __init__(self, name, fuel, reliability = 0):
        super().__init__(name, fuel)
        self.reliability = 0

    def drive(self, distance):
        random_number = random.randint(0,100)
        if random_number < float(self.reliability):
            driven_distance = super().drive(distance)
        else:
            driven_distance = 0
        return driven_distance
