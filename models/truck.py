from models import Car


class Truck(Car):
    def __init__(self, license_plate, car_type, rental_price, load_capacity):
        super().__init__(license_plate, car_type, rental_price)
        self.load_capacity = load_capacity

    def __str__(self):
        return f"Truck: {self.car_type}, License Plate: {self.license_plate}, Rental Price: {self.rental_price} per day, Load Capacity: {self.load_capacity} kg"
