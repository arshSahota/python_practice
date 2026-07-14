data = [
    {"cpu": 50, "memory": 60},
    {"cpu": 90},
    {"memory": 40}
]

def get_complete_records(data):

    complete = []

    for reading in data:
        if "cpu" in reading and "memory" in reading:
            complete.append(reading)

    return complete

print(get_complete_records(data))