from datetime import date, datetime
from models.rental import Rental


class RentalService:
    def __init__(self, car_rental):
        self._car_rental = car_rental

    @property
    def car_rental(self):
        return self._car_rental

    # Can delete car rental
    def can_delete_rental(self):
        if self.car_rental.cars:
            print("❌ Cannot delete: rental has cars.")
            return False
        if self.car_rental.rentals:
            print("❌ Cannot delete: rental has bookings.")
            return False
        return True

    # Find car by licence plate
    def find_car_by_license_plate(self, plate):
        for car in self._car_rental.cars:
            if car.license_plate == plate:
                return car
        return None

    # Find rental by date
    def find_rentals_by_date(self, date):
        return [r for r in self._car_rental.rentals if r.rental_date == date]

    # Create rental
    def create_rental(self, car, customer, rental_date):
        today = date.today()
        rental_dt = datetime.strptime(rental_date, "%Y-%m-%d").date()

        if rental_dt < today:
            raise ValueError("❌ Cannot rent for a past date.")

        for rental in self._car_rental.rentals:
            if rental.car == car and rental.rental_date == rental_date:
                raise ValueError("❌ Car is already rented for this date.")

        rental = Rental(car, customer, rental_date)
        self._car_rental.add_rental(rental)
        return rental
