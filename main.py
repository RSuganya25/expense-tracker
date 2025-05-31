from tracker import create_table, add_expense, view_expenses, delete_expense

# Create table if it doesn't exist yet
create_table()

# Add some expenses
add_expense('2025-05-31', 'Groceries', 25.50, 'Milk and Bread')
add_expense('2025-06-01', 'Transport', 15.00, 'Bus ticket')
add_expense('2025-06-02', 'Dining', 45.75, 'Dinner at restaurant')
add_expense('2025-06-03', 'Utilities', 60.00, 'Electricity bill')
add_expense('2025-06-04', 'Groceries', 30.20, 'Vegetables and fruits')
add_expense('2025-06-05', 'Entertainment', 20.00, 'Movie ticket')

print("Expenses before deletion:")
expenses = view_expenses()
for expense in expenses:
    print(expense)

# Delete expense with ID 2 (example)
delete_expense(2)

print("\nExpenses after deletion of ID 6:")
expenses = view_expenses()
for expense in expenses:
    print(expense)
