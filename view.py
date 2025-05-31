from tracker import view_expenses

def print_expenses():
    expenses = view_expenses()
    if not expenses:
        print("No expenses found.")
    else:
        for expense in expenses:
            print(f"ID: {expense[0]}, Date: {expense[1]}, Category: {expense[2]}, Amount: ${expense[3]:.2f}, Description: {expense[4]}")

if __name__ == "__main__":
    print_expenses()

