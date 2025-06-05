from tracker import create_table, add_expense, view_expenses, update_expense, delete_expense
from analysis import view_sorted_by_date, view_total_by_category

def get_valid_date(prompt):
    while True:
        date = input(prompt).strip()
        if len(date) == 10 and date[4] == '-' and date[7] == '-':
            return date
        else:
            print("Invalid date format. Please enter date as YYYY-MM-DD.")

def get_nonempty_input(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        else:
            print("This field cannot be empty. Please enter a valid value.")

def get_valid_float(prompt):
    while True:
        value = input(prompt).strip()
        try:
            fvalue = float(value)
            return fvalue
        except ValueError:
            print("Invalid amount. Please enter a valid number.")

def get_valid_int(prompt):
    while True:
        value = input(prompt).strip()
        try:
            ivalue = int(value)
            return ivalue
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def main():
    create_table()

    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Update Expense")
        print("4. Delete Expense")
        print("5. View Expenses Sorted by Date")
        print("6. View Total Expenses by Category")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ").strip()

        if choice == '1':
            date = get_valid_date("Enter date (YYYY-MM-DD): ")
            category = get_nonempty_input("Enter category: ")
            amount = get_valid_float("Enter amount: ")
            description = get_nonempty_input("Enter description: ")
            add_expense(date, category, amount, description)
            print("Expense added successfully!")

        elif choice == '2':
            print("\nAll Expenses:")
            for expense in view_expenses():
                print(expense)

        elif choice == '3':
            print("\nAll Expenses:")
            for expense in view_expenses():
                print(expense)
            id = get_valid_int("Enter ID of the expense to update: ")
            date = get_valid_date("Enter new date (YYYY-MM-DD): ")
            category = get_nonempty_input("Enter new category: ")
            amount = get_valid_float("Enter new amount: ")
            description = get_nonempty_input("Enter new description: ")
            update_expense(id, date, category, amount, description)
            print(f"Expense with ID {id} updated successfully!")

        elif choice == '4':
            print("\nAll Expenses:")
            for expense in view_expenses():
                print(expense)
            id = get_valid_int("Enter ID of the expense to delete: ")
            delete_expense(id)
            print(f"Expense with ID {id} deleted successfully!")

        elif choice == '5':
            print("\nExpenses Sorted by Date:")
            for expense in view_sorted_by_date():
                print(expense)

        elif choice == '6':
            print("\nTotal Expenses by Category:")
            for row in view_total_by_category():
                print(f"{row[0]}: ${row[1]:.2f}")

        elif choice == '7':
            print("Exiting program. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 7.")

if __name__ == "__main__":
    main()
