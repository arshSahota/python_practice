students = {
    "A": 85,
    "B": 92,
    "C": 78,
    "D": 92
}

toppers = []

highest_score = 0

for student in students:
    if highest_score <= students.get(student, 0):
        highest_score = students.get(student, 0)

    toppers.append(students[student])
    
print(toppers)