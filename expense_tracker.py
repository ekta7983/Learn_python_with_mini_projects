expenses = []

def show_menu():
    print("===================================================")
    print("                 Expense Tracker                    \n")
    print("1. Add Expense")
    print("2. View Total Expense")
    print("3. View All Expenses")
    print("4. Exit\n")

def add_expense():
    category = input("Enter the category:")
    amount = int(input("Enter the amount:"))
    expenses.append({
        "category":category,
        "amount":amount
    })
    print("\nExpenses added successfully!\n\n")

def view_all_expenses():
    print("\n")
    for expense in expenses:
        print(f"{expense}")
    print("\n\n")

while True:
    show_menu()
    choice = int(input("Enter your choice:"))

    if choice == 1:
        add_expense()

    elif choice == 2:
        total_expense = sum(expense["amount"] for expense in expenses)
        print(f"\nTotal expense: ${total_expense}\n\n")

    elif choice == 3:
        view_all_expenses()

    elif choice == 4:
        print("\nGoodbye!")
        break

    else:
        print("\nPlease enter a valid choice\n\n")

