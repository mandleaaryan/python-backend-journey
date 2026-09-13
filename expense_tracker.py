expenses = [
    {"item": "College Canteen", "amount": 120},
    {"item": "Metro", "amount": 50},
    {"item": "Coffee", "amount": 180},
    {"item": "Lunch", "amount": 150}
]

print("Expenses:")

for expense in expenses:
    print(expense["item"], "-", expense["amount"])