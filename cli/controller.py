from cli.menu import show_main_menu
from cli.rental_controller import _list_all_cars, _list_all_rentals, run_rental_menu
from models import CarRental
from services import RentalService


# Show main menu and navigation to next menu
def run_main_menu(rentals):
    while True:
        option = show_main_menu()

        # 1. Show all car rental companies with their cars
        if option == 1:
            _list_all_rentals_cars(rentals)
        # 2. Show all car rental companies with their bookings
        elif option == 2:
            _list_all_rentals_booking(rentals)
        # 3. Add a new car rental company
        elif option == 3:
            _add_new_car_rental(rentals)
        # 4.
        elif option == 4:
            _remove_car_rental(rentals)
        # 5. Select a car rental company
        elif option == 5:
            selected = _select_car_rental(rentals)
            if selected:
                run_rental_menu(selected)
        # 6. Exit"
        elif option == 6:
            print("👋 Goodbye!")
            break


# List all car rentals with their cars
def _list_all_rentals_cars(rental_list):
    print("\n✅ === All Cars in All Rentals ===")
    for rental in rental_list:
        _list_all_cars(rental)


# List all car rentals with their booking
def _list_all_rentals_booking(rental_list):
    print("\n📕 === All Booking in All Rentals ===")
    for rental in rental_list:
        _list_all_rentals(rental)


# Add a new car rental
def _add_new_car_rental(rental_list):
    print("\n➕ === Add New Car Rental ===")
    name = input("🏷️  Rental name: ")

    for rental in rental_list:
        if rental.rental_name == name:
            print("⚠️ A rental with this name already exists.")
            return

    new_rental = CarRental(name)
    rental_list.append(new_rental)
    print(f"✅ Car rental '{name}' added successfully.")


# Remove car rental
def _remove_car_rental(rental_list: list[CarRental]):
    print("\n🗑️ Remove Car Rental")

    if not rental_list:
        print("⚠️ No car rentals to remove.")
        return

    for idx, rental in enumerate(rental_list, 1):
        print(f"{idx}. {rental.rental_name}")

    try:
        choice = int(input("👉 Choose a rental number to remove: "))
        if 1 <= choice <= len(rental_list):
            selected = rental_list[choice - 1]
            service = RentalService(selected)

            if service.can_delete_rental():
                rental_list.pop(choice - 1)
                print(f"✅ Car rental '{selected.rental_name}' removed.")
            else:
                print("⚠️ Deletion aborted.")
        else:
            print("❌ Invalid selection.")
    except ValueError:
        print("❌ Invalid input. Please enter a number.")


# Select car rental
def _select_car_rental(rental_list):
    if not rental_list:
        print("⚠️ No car rentals available.")
        return None

    print("\n📂 === Select a Car Rental ===")
    for idx, rental in enumerate(rental_list, start=1):
        print(f"{idx}. {rental.rental_name}")

    try:
        choice = int(input("👉 Choose a rental number: "))
        if 1 <= choice <= len(rental_list):
            print(f"✅ Selected: {rental_list[choice - 1].rental_name}")
            return rental_list[choice - 1]
        else:
            print("❌ Invalid selection.")
            return None
    except ValueError:
        print("❌ Invalid input. Please enter a number.")
        return None
