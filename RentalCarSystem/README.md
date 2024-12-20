
# Car Rental System: Digital Application Development Project

## Overview
This project is part of the **24LLP109 – Digital Application Development** module at Loughborough University London. It demonstrates a **Car Rental System** developed using **Object-Oriented Programming (OOP)** principles. The system allows customers to rent, return, and inquire about cars through a command-line interface.

The project is divided into two parts:
1. **Software Development (60%)**: Creation of a functional car rental system in Python.
2. **Report (40%)**: A 2000-word analysis of the software development process.

---

## Features
1. **Customer Actions:**
   - Rent a car (Hatchback, Sedan, SUV) for a specified number of days.
   - Return a rented car and receive a detailed bill.
   - View available cars and pricing.
2. **Car Rental Shop:**
   - Manage car inventory dynamically.
   - Generate bills based on the rental duration and car type.
3. **VIP Customers:**
   - VIP members benefit from special discounted rates.
4. **Command-Line Interface**:
   - User-friendly prompts for interaction.

---

## Project Structure
The project contains the following main components:

- **Classes**:
  - `Customer`: Handles customer-related actions.
  - `RentalShop`: Manages inventory and billing.
  - `VIPCustomer`: A subclass of `Customer` for handling VIP-specific pricing.
- **Main Script**:
  - `main.py`: The entry point to interact with the system.
- **Inheritance**:
  - VIP-specific logic is implemented via inheritance from the base `Customer` class.
  
### Initial Inventory
- 4 Hatchbacks
- 3 Sedans
- 3 SUVs

---

## How to Run the Project
1. Clone this repository:
   ```bash
   git clone https://github.com/your-repository-link.git
   ```
2. Navigate to the project directory:
   ```bash
   cd car-rental-system
   ```
3. Run the main script:
   ```bash
   python main.py
   ```
4. Follow the on-screen prompts to interact with the system:
   - Rent a car
   - View inventory
   - Return a car
   - Exit

---

## Pricing Rules
### Regular Rates:
- **Hatchback**: £30/day (< 7 days), £25/day (≥ 7 days)
- **Sedan**: £50/day (< 7 days), £40/day (≥ 7 days)
- **SUV**: £100/day (< 7 days), £90/day (≥ 7 days)

### VIP Rates:
- **Hatchback**: £20/day
- **Sedan**: £35/day
- **SUV**: £80/day

---

## Example Usage
1. Rent a Sedan for 5 days:
   - Input: `1` → `Sedan` → `5`
   - Output: "You have rented a Sedan for 5 days. You will be charged £50 per day. We hope you enjoy our service."
2. View available inventory:
   - Input: `2`
   - Output: Inventory of available cars.
3. Return a Sedan after 5 days:
   - Input: `3` → `Sedan`
   - Output: Detailed bill.

---

## Key Concepts Demonstrated
- **Object-Oriented Design**:
  - Classes and inheritance for modularity and reusability.
- **Data Structures**:
  - Lists and dictionaries to manage inventory and customer data.
- **Control Flow**:
  - Conditional statements and loops for system logic.

---

## Screenshots
Screenshots showcasing the functionality of the system (renting, returning, viewing inventory, and exiting) are included in the project documentation.

---

## Limitations & Future Work
- Currently, only one car type can be rented per transaction.
- Enhancements can include:
  - Graphical User Interface (GUI) integration.
  - Multi-user and real-time updates for concurrent rentals.
  - Extended loyalty programs for VIPs.

---

## Submission Instructions
1. Submit a **zipped folder** containing:
   - Python source code files (`.py`).
   - Report (`.pdf`), named `<your_id_number>.pdf`.
2. Ensure the project can run independently without external dependencies.

---

## License
This project is for educational purposes and follows Loughborough University London's academic guidelines. Unauthorized distribution or plagiarism is strictly prohibited.
