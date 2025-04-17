from models import Car


class PassengerCar(Car):
    def __init__(self, license_plate, car_type, rental_price, number_of_doors):
        super().__init__(license_plate, car_type, rental_price)
        self.number_of_doors = number_of_doors

    def __str__(self):
        return f"Passenger Car: {self.car_type}, License Plate: {self.license_plate}, Rental Price: {self.rental_price} per day, Number of Doors: {self.number_of_doors}"
