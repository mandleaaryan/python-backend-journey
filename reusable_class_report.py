def count_passed(students):
    count = 0

    for student in students:
        if student["average"] >= 85:
            count += 1

    return count


def calculate_class_average(students):
    total = 0

    for student in students:
        total += student["average"]

    return total / len(students)


def generate_report(class_name, students):
    print("Class:", class_name)
    print("Passed:", count_passed(students))
    print("Average:", calculate_class_average(students))


class_a = [
    {"name": "Aaryan", "average": 90},
    {"name": "Tokyo", "average": 80}
]

class_b = [
    {"name": "Japan", "average": 95},
    {"name": "Delhi", "average": 85},
    {"name": "Osaka", "average": 70}
]

generate_report("Class A", class_a)

generate_report("Class B", class_b)