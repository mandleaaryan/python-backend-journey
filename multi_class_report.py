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


class_a = [
    {"name": "Aaryan", "average": 90},
    {"name": "Tokyo", "average": 80}
]

class_b = [
    {"name": "Japan", "average": 95},
    {"name": "Delhi", "average": 85},
    {"name": "Osaka", "average": 70}
]

print("Class A Passed:", count_passed(class_a))
print("Class A Average:", calculate_class_average(class_a))

print("Class B Passed:", count_passed(class_b))
print("Class B Average:", calculate_class_average(class_b))