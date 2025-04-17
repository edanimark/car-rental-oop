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
├── data/                       # Placeholder for future data storage
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

The app starts with 1 rental company, 3 test cars, and 4.

## 🧪 Example Flow

- Select a car rental company
- View cars / Add a new car
- Rent a car by selecting from the list
- Cancel bookings from the rental history
- Manage everything using intuitive menus

## 📋 Sample Dummy Data

```python
car1 = PassengerCar("ABC-123", "Sedan", 50, 4)
car2 = Truck("DEF-456", "Truck", 80, 5.0)
rental = CarRental("City Cars")
```

## 📂 Modules Overview

| Folder      | Purpose                                          |
| ----------- | ------------------------------------------------ |
| `models/`   | Domain classes (Car, Truck, Rental, CarRental)   |
| `services/` | RentalService with business logic                |
| `cli/`      | User interaction, menu navigation                |
| `data/`     | Reserved for future data persistence (JSON / DB) |

## 🧠 Design Considerations

- Follows SOLID OOP design principles
- RentalService separates business logic from CLI
- Controllers manage input/output cleanly
- Easy to extend with database or web frontend in future

---

Made with ❤️ for educational purposes.
