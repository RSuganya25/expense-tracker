# Expense Tracker

A simple Python-based Expense Tracker application using SQLite to record, update, delete, and view daily expenses.

## Features

- ✅ Add new expenses with date, category, amount, and description  
- ✅ View all recorded expenses  
- ✅ Update existing expenses  
- ✅ Delete expenses by ID  
- ✅ Auto-creates SQLite database and table if they don't exist  
- ✅ Clean console view with formatted output (`view.py`)  
- ✅ Modularized structure for maintainability  
- ✅ Uses SQLite (`data/expenses.db`) for storage  
- ✅ Lightweight – only uses Python's built-in `sqlite3` module (no extra dependencies)  
- ✅ **Input validation included** to ensure date format, non-empty fields, and valid numeric amounts to prevent errors during data entry  

## Getting Started

### Prerequisites

- Python 3.x installed on your system  
- VS Code or any code editor  
- Basic knowledge of running Python scripts from terminal

### Setup Instructions

1. Clone the repository:
    ```bash
    git clone git@github.com:RSuganya25/expense-tracker.git
    cd expense-tracker
    ```

2. Make sure the `data` folder exists to store your SQLite database:
    ```bash
    mkdir -p data
    ```

3. Run the main script to create the database and use the interactive CLI with input validation:
    ```bash
    python3 main.py
    ```

4. To view formatted expenses separately:
    ```bash
    python3 view.py
    ```

## File Structure

expense-tracker/  
│  
├── data/  
│ └── expenses.db # SQLite database file (auto-generated)  
│  
├── main.py # Interactive CLI script with input validation  
├── tracker.py # Core functions for CRUD operations with SQLite  
├── view.py # Nicely formats and prints expenses to console  
├── .gitignore # Prevents tracking DB, pycache, logs, etc.  
└── README.md # This documentation

## How to Use

- Import functions from `tracker.py` in your own Python scripts:  
  - `add_expense(date, category, amount, description)`  
  - `view_expenses()`  
  - `update_expense(id, date, category, amount, description)`  
  - `delete_expense(id)`  

- Use `main.py` to run the interactive CLI with input validation for safe data entry.  
- Use `view.py` to quickly display all your saved expenses in a human-readable format.

## Input Validation Details

- **Date validation:** Ensures the date is entered in the `YYYY-MM-DD` format.  
- **Non-empty validation:** Ensures fields like category and description are not left blank.  
- **Amount validation:** Ensures the amount entered is a valid number (float).

These validations help prevent runtime errors and improve user experience during data entry in the terminal.

## Notes

- The `__pycache__` folder and `.pyc` files are Python bytecode cache files and are ignored by Git.  
- The `.gitignore` excludes database files (`data/*.db`), `.env`, log files, and editor configurations.  
- Customize `main.py` to add or test additional features.

## License

This project is open source and available under the MIT License.

