data = [
    {"cpu": 50, "memory": 60},
    {"cpu": 90, "memory": 40},
    {"cpu": 70, "memory": 70}
]

def count_healthy(data):
    
    count = 0

    for reading in data:
        if reading["cpu"] < 80 and reading["memory"] < 80:
            count+=1

    return count

print(count_healthy(data))

