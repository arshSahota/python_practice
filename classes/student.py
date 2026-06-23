class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def __str__(self):
        return f"Student(name = {self.name}, grade = {self.grade})"
    
student1 = Student("Arshdeep", 98)
student2 = Student("Gursharan", 90)

print(student1)