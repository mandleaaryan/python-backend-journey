student = {
    "name": "Aaryan",
    "marks": [85, 92, 96]
}

print("Name:", student["name"])

total = 0

for mark in student["marks"]:
    total += mark

average = total / len(student["marks"])

print("Total:", total)
print("Average:", average)