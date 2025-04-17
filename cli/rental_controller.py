from datetime import datetime

from cli.menu import show_rental_menu
from models import PassengerCar, Truck
from services import RentalService


# Show rental menu and operations
def run_rental_menu(rental):
    service = RentalService(rental)
    while True:
        option = show_rental_menu(rental.rental_name)

        # 1. List all cars
        if option == 1:
            _list_all_cars(rental)
        # 2. Add a car to this company
        elif option == 2:
            _add_car_to_rental(rental)
        # 3. Remove a car from this company
        elif option == 3:
            _remove_car_from_rental(rental)
        # 4. Rent out a car (passenger or truck)
        elif option == 4:
            _rent_a_car(service)
        # 5. List all bookings
        elif option == 5:
            _list_all_rentals(rental)
        # 6. Cancel a booking"
        elif option == 6:
            _remove_rental(service)
        # 7. Back to main menu
        elif option == 7:
            break


# List all cars for rental
def _list_all_cars(rental):
    print(f"\n🚗 === Cars in {rental.rental_name} ===")
    cars = rental.cars
    if cars:
        for car in cars:
            print(f"  → {car}")
    else:
        print("⚠️ No cars in this rental.")


# Add a new car
def _add_car_to_rental(rental):
    print("\n➕ === Add New Car ===")
    license_plate = input("🏷️  License plate: ")
    print("🚘 Select car type:")
    print("1. Passenger Car")
    print("2. Truck")

    while True:
        car_type_option = input("👉 Choose (1 or 2): ")
        if car_type_option not in ("1", "2"):
            print("❌ Invalid choice. Please enter 1 or 2.")
        else:
            break

    while True:
        try:
            rental_price = float(input("💰 Rental price per day: "))
            break
        except ValueError:
            print("❌ Invalid input. Please enter a valid number.")

    if car_type_option == "2":
        while True:
            try:
                capacity = float(input("📦 Capacity (tons): "))
                car = Truck(license_plate, "Truck", rental_price, capacity)
                break
            except ValueError:
                print("❌ Invalid input. Please enter a valid number.")
    else:
        while True:
            try:
                doors = int(input("🚪 Number of doors: "))
                car = PassengerCar(license_plate, "Passenger", rental_price, doors)
                break
            except ValueError:
                print("❌ Invalid input. Please enter a valid integer.")

    rental.add_car(car)
    print(f"✅ Car {license_plate} added to {rental.rental_name}.")


# Remove car from car rental
def _remove_car_from_rental(rental):
    print("\n🗑️ === Remove Car from Rental ===")
    cars = rental.cars
    if not cars:
        print("⚠️ No cars to remove.")
        return

    for idx, car in enumerate(cars, 1):
        print(f"{idx}. {car}")

    try:
        choice = int(input("👉 Choose a car to remove by number: "))
        if 1 <= choice <= len(cars):
            selected_car = cars[choice - 1]
            success = rental.remove_car(selected_car.license_plate)
            if success:
                print(f"✅ Car {selected_car.license_plate} removed.")
            else:
                print("❌ Cannot remove car: it may have rentals.")
        else:
            print("❌ Invalid selection.")
    except ValueError:
        print("❌ Please enter a number.")


# Rent a car
def _rent_a_car(service):
    print("\n📝 === Rent a Car ===")
    cars = service.car_rental.cars
    if not cars:
        print("⚠️ No cars available.")
        return

    for idx, car in enumerate(cars, 1):
        print(f"{idx}. {car}")

    try:
        choice = int(input("👉 Choose a car to rent by number: "))
        if 1 <= choice <= len(cars):
            selected_car = cars[choice - 1]
        else:
            print("❌ Invalid selection.")
            return
    except ValueError:
        print("❌ Please enter a number.")
        return

    customer = input("👤 Customer name: ")
    rental_date = _get_valid_date()

    try:
        rental = service.create_rental(selected_car, customer, rental_date)
        print(f"✅ Rental created: {rental}")
    except Exception as e:
        print(f"❌ Failed to create rental: {e}")


# Get valid date
def _get_valid_date(prompt="📅 Enter date (YYYY-MM-DD): ") -> str:
    while True:
        date_str = input(prompt)
        try:
            datetime.strptime(date_str, "%Y-%m-%d")
            return date_str
        except ValueError:
            print("❌ Invalid date format. Please use YYYY-MM-DD.")


# List all rentals
def _list_all_rentals(rental):
    print(f"\n📜 === Rentals in {rental.rental_name} ===")
    rentals = rental.rentals
    if rentals:
        for rental_obj in rentals:
            print(f"  → {rental_obj}")
    else:
        print("⚠️ No rentals found.")


# Remove rental
def _remove_rental(service):
    print("\n🗑️ Remove Rental")

    rentals = service.car_rental.rentals
    if not rentals:
        print("⚠️ No bookings to remove.")
        return

    print("📜 Existing Rentals:")
    for idx, rental in enumerate(rentals, 1):
        print(f"{idx}. {rental}")

    try:
        choice = int(input("👉 Choose a rental to remove by number: "))
        if 1 <= choice <= len(rentals):
            selected_rental = rentals.pop(choice - 1)
            print(f"✅ Removed: {selected_rental}")
        else:
            print("❌ Invalid selection.")
    except ValueError:
        print("❌ Please enter a number.")
