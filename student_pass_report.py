def is_passed(average):
    return average >= 85

students = [
    {"name": "Aaryan", "average": 90},
    {"name": "Tokyo", "average": 83},
    {"name": "Japan", "average": 91},
    {"name": "Delhi", "average": 78}
]

count = 0

for student in students:
    if is_passed(student["average"]):
        print(student["name"])
        count += 1

print("Passed:", count)