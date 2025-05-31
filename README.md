# Expense Tracker

A simple Python-based Expense Tracker application using SQLite to record, update, delete, and view daily expenses.

## Features

- Add new expenses with date, category, amount, and description
- View all recorded expenses
- Update existing expenses
- Delete expenses
- Uses SQLite database (`data/expenses.db`) for storage
- Simple Python scripts with built-in `sqlite3` module (no extra dependencies)

## Getting Started

### Prerequisites

- Python 3.x installed on your computer  
- VS Code or any code editor for editing scripts  
- Basic knowledge of running Python scripts from terminal

### Setup

1. Clone the repository:
    ```bash
    git clone git@github.com:RSuganya25/expense-tracker.git
    cd expense-tracker
    ```

2. Make sure the `data` folder exists:
    ```bash
    mkdir -p data
    ```

3. Run the Python script to create the database and add a sample expense:
    ```bash
    python3 main.py
    ```

4. You can modify `main.py` to test other functions like viewing, updating, or deleting expenses.

## File Structure

expense-tracker/
│
├── data/
│ └── expenses.db # SQLite database file (auto-created)
│
├── tracker.py # Core functions to interact with SQLite
├── main.py # Example script to test tracker functions
└── README.md # This file


## How to Use

- Import functions from `tracker.py` in your own Python scripts  
- Use `add_expense()`, `view_expenses()`, `update_expense()`, and `delete_expense()` to manage expenses

## Notes

- The `__pycache__` folder and `.pyc` files are auto-generated Python bytecode cache files and can be ignored.  
- The `.gitignore` file excludes `__pycache__` and database files by default (optional).

## License

This project is open source and available under the MIT License.

