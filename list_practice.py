marks = [85, 92, 78, 96, 88]

total = 0

for mark in marks:
    total += mark

average = total / len(marks)

print("Marks:", marks)
print("Total:", total)
print("Average:", average)

highest = marks[0]

for mark in marks:
    if mark > highest:
        highest = mark

print("Highest:", highest)