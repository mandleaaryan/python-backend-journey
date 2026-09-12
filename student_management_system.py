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


def calculate_class_average(students):
    total = 0

    for student in students:
        total += student["average"]

    return total / len(students)


def show_students(students):
    print("\nStudents:")

    for student in students:
        print(student["name"], "-", student["average"])


def generate_report(students):
    print("\nClass Report")
    print("Passed Students:", count_passed(students))
    print("Top Student:", find_top_student(students)["name"])
    print("Class Average:", calculate_class_average(students))


students = [
    {"name": "Aaryan", "average": 90},
    {"name": "Tokyo", "average": 80},
    {"name": "Japan", "average": 95},
    {"name": "Delhi", "average": 85}
]

show_students(students)

generate_report(students)