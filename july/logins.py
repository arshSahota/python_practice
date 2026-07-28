logins = [
    {"user": "Alice", "date": "2024-01-01"},
    {"user": "Bob", "date": "2024-01-01"},
    {"user": "Alice", "date": "2024-01-02"},
    {"user": "Charlie", "date": "2024-01-01"},
    {"user": "Bob", "date": "2024-01-02"},
    {"user": "Bob", "date": "2024-01-02"},
]

def unique_logins(logins):

    unique_logins = {}

    for login in logins:
        user = login["user"]
        date = login["date"]

        if user not in unique_logins:
            unique_logins[user] = set()

        unique_logins[user].add(date)

    max_days = 0
    most_active = ""

    for user in unique_logins:
        days = len(unique_logins[user])

        if days > max_days:
            max_days = days
            most_active = user
        elif days == max_days and user > most_active:
            most_active = user

    return most_active


print(unique_logins(logins))