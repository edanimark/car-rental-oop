# 🚗 Car Rental CLI Application

This is a console-based car rental system implemented in Python using object-oriented programming principles.  
The application supports multiple rental companies, vehicle management, and booking functionality.

## 📦 Features

- Manage multiple car rental companies
- Add and remove cars (PassengerCar / Truck)
- Rent cars for a specific date
- Cancel bookings
- List all cars and bookings
- User-friendly CLI navigation with numbered selection menus

## 🧱 Architecture

The application follows a modular structure:

```
.
├── main.py                      # Entry point with dummy data
├── models/                     # OOP models (Car, Rental, etc.)
├── services/                   # Business logic (RentalService)
├── cli/                        # CLI UI + controllers (menus, input, logic)
├── README.md                   # This file
```

## 🛠️ Technologies

- Python 3.11+
- OOP (abstract classes, inheritance, encapsulation)
- CLI-based interaction
- Clean modular separation (MVC-ish)

## 🚀 Getting Started

### 1. Clone the repository:

```bash
git clone git@github.com:edanimark/car-rental-oop.git
cd car-rental-oop
```

### 2. Run the application:

You can run the CLI program in two ways:

#### ▶️ a) From terminal:

```bash
python main.py
```

#### 🐞 b) From debugger (recommended for development):

- Open the project in an IDE like **VS Code** or **PyCharm**
- Set breakpoints where needed (e.g., in `main.py`, `controller.py`)
- Run using the debugger to inspect runtime behavior

This is useful for:

- Stepping through the flow
- Viewing object states
- Testing input/output paths interactively

The app starts with 1 rental company, 3 cars, and 4 booking.

## 🧪 Example Flow

- Select a car rental company
- View cars / Add a new car
- Rent a car by selecting from the list
- Cancel bookings from the rental history
- Manage everything using intuitive menus

## 📋 Sample Dummy Data

```python
car1 = PassengerCar("ABC-123", "Passenger", 50, 4)
car2 = PassengerCar("ABC-456", "Passenger", 50, 4)
car3 = Truck("ABC-101", "Truck", 80, 5.0)

rental1 = Rental(car1, "Test Elek", "2025-06-01")
rental2 = Rental(car1, "Nagy Jakab", "2025-06-02")
rental3 = Rental(car2, "Kis Béla", "2025-06-01")
rental4 = Rental(car3, "Közepes János", "2025-06-02")

car_rental = CarRental("City Cars")
```

## 📂 Modules Overview

| Folder      | Purpose                                        |
| ----------- | ---------------------------------------------- |
| `models/`   | Domain classes (Car, Truck, Rental, CarRental) |
| `services/` | RentalService with business logic              |
| `cli/`      | User interaction, menu navigation              |

## 🧠 Design Considerations

- Follows SOLID OOP design principles
- RentalService separates business logic from CLI
- Controllers manage input/output cleanly
- Easy to extend with database or web frontend in future

---

Made with ❤️ for educational purposes.
