from cli import run_main_menu
from models import PassengerCar, Truck, CarRental, Rental


def init_dummy_data():
    car1 = PassengerCar("ABC-123", "Passenger", 50, 4)
    car2 = PassengerCar("ABC-456", "Passenger", 50, 4)
    car3 = Truck("ABC-101", "Truck", 80, 5.0)

    rental1 = Rental(car1, "Test Elek", "2025-06-01")
    rental2 = Rental(car1, "Nagy Jakab", "2025-06-02")
    rental3 = Rental(car2, "Kis Béla", "2025-06-01")
    rental4 = Rental(car3, "Közepes János", "2025-06-02")

    car_rental = CarRental("City Cars")

    car_rental.add_car(car1)
    car_rental.add_car(car2)
    car_rental.add_car(car3)

    car_rental.add_rental(rental1)
    car_rental.add_rental(rental2)
    car_rental.add_rental(rental3)
    car_rental.add_rental(rental4)

    rental_list = [car_rental]
    return rental_list


def main():
    # Init dummy data
    rentals = init_dummy_data()

    # Main menu
    run_main_menu(rentals)


if __name__ == "__main__":
    main()
