
transactions = []

def add_transaction():
    transaction_type = input("Enter type (income/expense): ").lower()
    category = input("Enter category: ")
    amount = float(input("Enter amount: ₹"))

    if transaction_type not in ["income", "expense"]:
        print("Invalid transaction type!")
        return

    if amount <= 0:
        print("Amount must be greater than zero!")
        return

    transactions.append({
        "type": transaction_type,
        "category": category,
        "amount": amount
    })

    print("Transaction added successfully!")


def view_transactions():
    if not transactions:
        print("No transactions found.")
        return

    for i, item in enumerate(transactions, start=1):
        print(
            f"{i}. {item['type'].title()} | "
            f"{item['category']} | ₹{item['amount']:.2f}"
        )


def show_summary():
    income = sum(
        item["amount"] for item in transactions
        if item["type"] == "income"
    )

    expenses = sum(
        item["amount"] for item in transactions
        if item["type"] == "expense"
    )

    print("\n----- FINANCIAL SUMMARY -----")
    print(f"Total Income: ₹{income:.2f}")
    print(f"Total Expenses: ₹{expenses:.2f}")
    print(f"Remaining Balance: ₹{income - expenses:.2f}")


def search_category():
    category = input("Enter category to search: ").lower()

    found = False
    for item in transactions:
        if item["category"].lower() == category:
            print(item)
            found = True

    if not found:
        print("No transactions found in this category.")


def delete_transaction():
    view_transactions()

    if not transactions:
        return

    try:
        number = int(input("Enter transaction number to delete: "))

        if 1 <= number <= len(transactions):
            removed = transactions.pop(number - 1)
            print("Deleted:", removed)
        else:
            print("Invalid transaction number!")

    except ValueError:
        print("Please enter a valid number!")


while True:
    print("\n===== EXPENSE MANAGEMENT SYSTEM =====")
    print("1. Add Transaction")
    print("2. View Transactions")
    print("3. Financial Summary")
    print("4. Search by Category")
    print("5. Delete Transaction")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_transaction()
    elif choice == "2":
        view_transactions()
    elif choice == "3":
        show_summary()
    elif choice == "4":
        search_category()
    elif choice == "5":
        delete_transaction()
    elif choice == "6":
        print("Thank you for using Expense Tracker!")
        break
    else:
        print("Invalid choice! Try again.")
