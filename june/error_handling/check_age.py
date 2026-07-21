def check_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    return age

try:
    print(check_age(-1))
except ValueError as e:
    print("Error", e)