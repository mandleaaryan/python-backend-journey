def calculate_average(marks):
    total = 0

    for mark in marks:
        total += mark

    return total / len(marks)

students = [
    {"name": "Aaryan", "marks": [80, 90, 100]},
    {"name": "Tokyo", "marks": [70, 85, 95]},
    {"name": "Japan", "marks": [88, 92, 94]}
]

for student in students:
    avg = calculate_average(student["marks"])

    print("Name:", student["name"])
    print("Average:", avg)
    print()