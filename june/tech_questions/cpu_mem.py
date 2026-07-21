data = [
    {"cpu": 50, "memory": 60},
    {"cpu": 90, "memory": 40},
    {"cpu": 70, "memory": 75},
    {"cpu": 85, "memory": 90}
]

CPU_THRESHOLD = 80
MEMORY_THRESHOLD = 80

def get_valid_readings(data, cpu_threshold, memory_threshold):
    valid = []

    for pair in data:
        if pair["cpu"] < cpu_threshold and pair["memory"] < memory_threshold:
            valid.append(pair)

    return valid

print(get_valid_readings(data, CPU_THRESHOLD, MEMORY_THRESHOLD))