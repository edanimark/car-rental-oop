class CarRental:
    def __init__(self, rental_name):
        self._rental_name = rental_name
        self._cars = []
        self._rentals = []

    @property
    def rental_name(self):
        return self._rental_name

    @property
    def cars(self):
        return self._cars

    @property
    def rentals(self):
        return self._rentals

    # Add car to car rental
    def add_car(self, car):
        self._cars.append(car)

    # Remove car from car rental
    def remove_car(self, license_plate):
        for car in self._cars:
            if car.license_plate == license_plate:
                # Check if this car has any rental
                for rental in self.rentals:
                    if rental.car == car:
                        print("❌ Cannot remove: car has active or historical rentals.")
                        return False
                self._cars.remove(car)
                return True
        return False

    # Add rental to rental
    def add_rental(self, rental):
        self._rentals.append(rental)

    # Remove rental
    def remove_rental(self, license_plate, rental_date):
        for rental in self.rentals:
            if (
                rental.car.license_plate == license_plate
                and rental.rental_date == rental_date
            ):
                self._rentals.remove(rental)
                print(f"✅ Rental for {license_plate} on {rental_date} removed.")
                return True
        print("❌ Rental not found.")
        return False

    def __str__(self):
        return f"Car Rental: {self.rental_name}"
