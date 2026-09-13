def calculate_total_expenses(expenses):
    total = 0

    for expense in expenses:
        total += expense["amount"]

    return total


def find_highest_expense(expenses):
    highest = expenses[0]

    for expense in expenses:
        if expense["amount"] > highest["amount"]:
            highest = expense

    return highest


def calculate_average_expense(expenses):
    total = calculate_total_expenses(expenses)

    return total / len(expenses)


def show_expenses(expenses):
    print("Expenses:")

    for expense in expenses:
        print(expense["item"], "-", expense["amount"])


def generate_report(expenses):
    highest = find_highest_expense(expenses)

    print("\nExpense Report")
    print("Total Spending:", calculate_total_expenses(expenses))
    print("Highest Expense:", highest["item"], "-", highest["amount"])
    print("Average Expense:", calculate_average_expense(expenses))


expenses = [
    {"item": "College Canteen", "amount": 120},
    {"item": "Metro", "amount": 50},
    {"item": "Coffee", "amount": 180},
    {"item": "Lunch", "amount": 150}
]

show_expenses(expenses)

generate_report(expenses)