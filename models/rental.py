class Rental:
    def __init__(self, car, customer, rental_date):
        self._car = car
        self._customer = customer
        self._rental_date = rental_date

    @property
    def car(self):
        return self._car

    @property
    def customer(self):
        return self._customer

    @property
    def rental_date(self):
        return self._rental_date

    def __str__(self):
        return f"Rental: {self.customer} rented {self.car} on {self.rental_date}"
