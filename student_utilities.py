def count_passed(students):
    count = 0

    for student in students:
        if student["average"] >= 85:
            count += 1

    return count


def find_top_student(students):
    top_student = students[0]

    for student in students:
        if student["average"] > top_student["average"]:
            top_student = student

    return top_student


students = [
    {"name": "Aaryan", "average": 90},
    {"name": "Tokyo", "average": 83},
    {"name": "Japan", "average": 91},
    {"name": "Delhi", "average": 78}
]

print("Passed:", count_passed(students))

top = find_top_student(students)

print("Top Student:", top["name"])
print("Average:", top["average"])