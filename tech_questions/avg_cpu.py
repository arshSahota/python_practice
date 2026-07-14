data = [
    {"cpu": 50},
    {"cpu": 70},
    {"cpu": 80}
]

def average_cpu(data):
    sum = 0
    for reading in data:
        sum+=reading["cpu"]

    return sum/len(data)

print(average_cpu(data))