class Employee:
    company = "Microsoft"

    def __init__(self, name, role):
        self.name = name
        self.role = role

    def __str__(self):
        return f"Employee(name={self.name}, role={self.role})"
        

Employee1 = Employee("Arshdeep", "Senior Software Engineer")
Employee2 = Employee("Gursharan", "Senior DevOps Engineer")

print(Employee1)

# print(f"This information is for {Employee1.name} who works at {Employee1.company} as {Employee1.role} ")
# print(f"This information is for {Employee2.name} who works at {Employee2.company} as {Employee2.role} ")