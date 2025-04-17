from abc import ABC, abstractmethod


# Abstract class
class Car(ABC):
    def __init__(self, license_plate, car_type, rental_price):
        self._license_plate = license_plate
        self._car_type = car_type  # passenger car or truck
        self._rental_price = rental_price

    @property
    def license_plate(self):
        return self._license_plate

    @property
    def car_type(self):
        return self._car_type

    @property
    def rental_price(self):
        return self._rental_price

    @abstractmethod
    def __str__(self):
        pass
