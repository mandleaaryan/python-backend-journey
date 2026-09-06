students = [
    {"name": "Aaryan", "average": 90},
    {"name": "Tokyo", "average": 83},
    {"name": "Japan", "average": 91},
    {"name": "Delhi", "average": 78}
]

passed = 0

for student in students:
    if student["average"] >= 85:
        print(student["name"])
        passed += 1

print("Passed:", passed)