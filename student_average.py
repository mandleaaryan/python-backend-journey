def calculate_average(marks):
    total = 0

    for mark in marks:
        total += mark

    return total / len(marks)

student = {
    "name": "Aaryan",
    "marks": [80, 90, 100]
}

avg = calculate_average(student["marks"])

print("Name:", student["name"])
print("Average:", avg)