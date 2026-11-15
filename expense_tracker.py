# Personal-Expense-Tracker

expenses = []

def add_expense():
    name = input("Enter expense name: ")
    amount = float(input("Enter amount: "))

    expense = {
        "name": name,
        "amount": amount
    }

    expenses.append(expense)
    print("Expense added successfully!")

def view_expenses():
    if not expenses:
        print("No expenses found!")
    else:
        print("\n--- YOUR EXPENSES ---")
        for i, expense in enumerate(expenses, 1):
            print(i, expense["name"], "-", expense["amount"])

def total_expenses():
    total = 0

    for expense in expenses:
        total += expense["amount"]

    print("Total Expenses:", total)

while True:
    print("\n--- PERSONAL EXPENSE TRACKER ---")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expenses")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        total_expenses()
    elif choice == "4":
        print("Thank you!")
        break
    else:
        print("Invalid choice!")
      
