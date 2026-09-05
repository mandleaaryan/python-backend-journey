students = [
    {"name": "Aaryan", "average": 90},
    {"name": "Tokyo", "average": 83},
    {"name": "Japan", "average": 91}
]

top_student = students[0]

for student in students:
    if student["average"] > top_student["average"]:
        top_student = student

print("Top Student:", top_student["name"])
print("Average:", top_student["average"])