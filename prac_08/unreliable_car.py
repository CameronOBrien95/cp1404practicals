from prac_08.car import Car
from random import randint


class UnreliableCar(Car):

    def __init__(self, name, fuel, reliability):
        """Initialise an unreliable Car instance, based on parent class Car"""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Returns distance driven, factoring in if the car is reliable"""
        random_number = randint(1, 100)
        if random_number >= self.reliability:
            distance = 0
        distance_driven = super().drive(distance)
        return distance_driven