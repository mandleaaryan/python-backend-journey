student = {
    "name": "Aaryan",
    "age": 23
}

student["country"] = "India"
student["age"] = 24

for key in student:
    print(key, ":", student[key])

print("Total fields:", len(student))