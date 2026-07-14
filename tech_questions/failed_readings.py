data = [
    {"cpu": 50, "memory": 60},
    {"cpu": 90, "memory": 40},
    {"cpu": 70, "memory": 95}
]

CPU_THRESHOLD = 80
MEMORY_THRESHOLD = 80

def get_failed_readings(data, cpu_thresh, mem_thresh):

    failed = []

    for reading in data:
        if reading["cpu"] > cpu_thresh or reading["memory"] > mem_thresh:
            failed.append(reading)

    return failed

print(get_failed_readings(data, CPU_THRESHOLD, MEMORY_THRESHOLD))
