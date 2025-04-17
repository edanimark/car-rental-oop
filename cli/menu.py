# Main menu for car rental system
def show_main_menu():
    print("\n🚗 === Car Rental System ===")
    print("1. 📗 Show all car rental companies with their cars")
    print("2. 📕 Show all car rental companies with their bookings")
    print("3. ➕ Add a new car rental company")
    print("4. 🗑️ Remove a car rental company")
    print("5. 📂 Select a car rental company")
    print("6. ❌ Exit")
    return _get_menu_choice()


# Rental menu for rental operations
def show_rental_menu(rental_name):
    print(f"\n📋 --- Rental Menu: {rental_name} ---")
    print("1. 🚘 List all cars")
    print("2. ➕ Add a car to this company")
    print("3. 🗑️ Remove a car from this company")
    print("4. 📝 Rent out a car (passenger or truck)")
    print("5. 📜 List all bookings")
    print("6. 🗑️ Cancel a booking")
    print("7. 🔙 Back to main menu")
    return _get_menu_choice()


# Get menu option from the user
def _get_menu_choice(prompt="👉 Choose an option: "):
    try:
        return int(input(prompt))
    except ValueError:
        print("❌ Invalid input. Please enter a number.")
        return -1
