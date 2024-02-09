# # List of dictionaries
students = [
    {"name": "Alice", "age": 22, "grade": 85},
    {"name": "Bob", "age": 20, "grade": 92},
    {"name": "Charlie", "age": 21, "grade": 78},
    {"name": "David", "age": 22, "grade": 95}
]

# Sorting the list of dictionaries based on the 'grade' key
sorted_students = sorted(students, key=lambda x: x['grade'])

# Displaying the sorted list
for student in sorted_students:
    print(student)


# Sorting the list of dictionaries based on the 'grade' key in descending order
sorted_students_desc = sorted(students, key=lambda x: x['grade'], reverse=True)

# Displaying the sorted list in descending order
for student in sorted_students_desc:
    print(student)

